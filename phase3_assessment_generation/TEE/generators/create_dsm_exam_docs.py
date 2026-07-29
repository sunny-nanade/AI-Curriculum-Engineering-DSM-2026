"""
DSM Exam Documentation Generator
===================================
Creates:
  1. DSM_Topic_Mapping.pdf   — question-wise topic list for all 3 sets in one file
  2. DSM_Student_Template.pdf — exam template for students (units, marks, COs; no exact questions)

Dynamic Systems Modeling (702MH0C025)
B.Tech Mechatronics, Semester IV, AY 2025-26
Dr. Sunny Nanade, Course Instructor
"""

from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.platypus import (SimpleDocTemplate, Table, TableStyle, Paragraph,
                                 Spacer, PageBreak, HRFlowable)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from pathlib import Path

OUT_DIR = Path(r"D:\sunny sir\Even Sem 2025-26\TEE\DSM\Final Papers")

# ─── Topic data extracted from all 3 sets ────────────────────────────────────
# Format: (Q_label, topic_A, topic_B, topic_C)

Q1_TOPICS = [
    ("Q1(a)\n[5M]",
     "Rigid Body Definitions\n(DOF, Rolling-without-slipping,\nInstantaneous Centre of Rotation)",
     "Holonomic vs Non-holonomic\nConstraints & DOF Formula\n(with examples)",
     "Three Damping Regimes\n(Underdamped / Critically-damped\n/ Overdamped; automotive context)"),

    ("Q1(b)\n[5M]",
     "Projectile Motion — Numerical\n(max height, time of flight,\nrange, velocity at t=1 s)",
     "2D Kinematics — Numerical\n(position, velocity, acceleration\nfrom parametric x(t), y(t))",
     "Rocket Kinematics — Numerical\n(v(t), a(t) from height function,\nmax height & time)"),

    ("Q1(c)\n[5M]",
     "Atwood Machine — Numerical\n(m₁=5 kg, m₂=3 kg;\nacceleration, tension, velocity @ 1.5 s)",
     "Block on 40° Rough Incline\n(normal force, friction force,\ndownward acceleration)",
     "Atwood Machine — Numerical\n(m₁=6 kg, m₂=4 kg;\nacceleration, tension, velocity @ 1 s)"),

    ("Q1(d)\n[5M]",
     "Work-Energy Theorem on Incline\n(rough 35° incline, block from rest,\nspeed after 4 m travel)",
     "Rotating Disk — Angular Dynamics\n(MOI, angular velocity, tangential\n& centripetal acceleration at rim)",
     "Coordinate Conversions\n(Cartesian→Polar 2D;\nCylindrical→Cartesian 3D)"),
]

Q2_TOPICS = [
    ("Q2(a)\n[5M]",
     "Frictionless Incline Block\n(acceleration, stopping distance,\ntime to stop; 30°, v₀=10 m/s)",
     "Vertical Circular Loop — R=8 m\n(min entry speed to complete loop;\nnormal force at top, m=2 kg)",
     "Rough Incline Block — Up & Slide\n(deceleration going up, check slide-back,\nrebound acceleration; 30°, μ_k=0.2)"),

    ("Q2(b)\n[5M]",
     "Block-and-Tackle Pulley — 4 pulleys\n(MA, system efficiency @95% each,\nactual force, heat wasted)",
     "Block-and-Tackle Pulley — 6 pulleys\n(MA, system efficiency @92% each,\nactual force, heat wasted; 2000 kg)",
     "Atwood-type Elevator System\n(loaded car vs counterweight;\nacceleration, cable tension)"),

    ("Q2(c)\n[5M]",
     "Vertical Circular Loop — R=2 m\n(min speed at top, min entry speed;\nnormal force @ bottom, v=12 m/s)",
     "Atwood Machine — m₁=7 kg, m₂=5 kg\n(acceleration, tension,\nvelocity @ 2 s; verify T range)",
     "Frictionless 30° Incline from Rest\n(normal force, acceleration,\nvelocity & distance at t=3 s)"),

    ("Q2(d)\n[5M]",
     "Movable Pulley System\n(constant-velocity force;\nacceleration for F=300 N; 50 kg load)",
     "CNC 3-Axis Linear Interpolation\n(travel distance, unit vector,\naxis speeds, move time)",
     "CNC Trapezoidal & Triangular Profiles\n(two move distances: 250 mm & 10 mm;\ntimes and peak velocities)"),
]

Q3_TOPICS = [
    ("Q3(a)\n[5M]",
     "Rolling Race on 30° Incline\n(solid sphere vs disk vs hollow cylinder;\nacceleration, time, velocity; winner?)",
     "Logarithmic Decrement\n(from successive amplitude peaks;\nζ, ω_n, f_n, spring stiffness)",
     "Solid Disk Rolling on 20° Incline\n(acceleration, velocity, time;\ncompare with frictionless sliding)"),

    ("Q3(b)\n[5M]",
     "Physical Pendulum\n(uniform rod pivoted at end;\nMOI, natural frequency, period;\ncompare with simple pendulum)",
     "Rolling Wheel — Acceleration Analysis\n(ω, α from center kinematics;\ntotal acceleration at top & bottom)",
     "Simple Pendulum Released from 60°\n(height gained, speed at bottom;\ntension in string at lowest point)"),

    ("Q3(c)\n[5M]",
     "Undamped Spring-Mass System\n(ω_n, period, max velocity,\ntotal mechanical energy)",
     "Rotating Disk with Viscous Friction\n(MOI, time constant,\nsteady-state angular velocity)",
     "Car Braking — Energy Method\n(KE from 100 km/h;\nstopping distance, heat dissipated)"),

    ("Q3(d)\n[5M]",
     "Spring-Mass-Damper — Classification\n(ω_n, c_cr, ζ, ω_d, system type;\ntime to decay to 10% amplitude)",
     "Two-Stage Gear Train\n(overall gear ratio, output RPM,\noutput torque, power balance)",
     "Damped Vibration Parameters\n(ω_n, ω_d, c_cr, c;\ncycles to halve amplitude)"),
]

Q4_TOPICS = [
    ("Q4(a)\n[5M]",
     "Transport Theorem — Derivation\n(vector in fixed vs rotating frame;\nvelocity relation, physical significance)",
     "Rigid Body Velocity Formula — Derivation\n(v_P = v_cm + ω×r;\nrolling constraint derivation)",
     "Moment of Inertia & Parallel Axis Theorem\n(definition, PAT statement;\nderive I for rod about centre & end)"),

    ("Q4(b)\n[5M]",
     "Acceleration in Rotating Frame\n(derive full equation;\nCoriolis, centripetal, Euler terms explained)",
     "Rotation Matrices & Gimbal Lock\n(R_x, R_y, R_z matrices;\ngimbal lock explained; quaternion fix)",
     "Slider-Crank Geometry — Theory\n(constraint equation, piston position;\nasymmetric motion & effect of L/r)"),

    ("Q4(c)\n[5M]",
     "Rotating Platform — Full Numerical\n(Coriolis, centripetal, relative;\ntotal acceleration; Ω=3 rad/s, r=1 m)",
     "Rolling Wheel — Velocity Analysis\n(velocities at top, bottom,\nright-side contact point; R=0.5 m)",
     "MOI Calculations — Multiple Shapes\n(disk, rod about centre/end, sphere;\nverify PAT for rod)"),

    ("Q4(d)\n[5M]",
     "Coriolis Deflection on Earth\n(latitude 45°N, v=500 m/s north;\na_Coriolis, lateral deflection @ 10 s)",
     "Rotating Rod — Kinematics\n(ω=5 rad/s, α=2 rad/s²;\nvelocities & accelerations at 3 positions)",
     "Slider-Crank at 6000 RPM, θ=90°\n(ω, φ, piston velocity;\ncheck if acceleration > 500 g at TDC)"),
]

Q5_TOPICS = [
    ("Q5(a)\n[5M]",
     "Euler-Lagrange Equation — Derivation\n(from Hamilton's principle;\ngeneralized coordinates, advantage)",
     "Work-Energy Theorem\n(statement, conservative vs\nnon-conservative forces, modified form)",
     "Simple Pendulum via Lagrangian\n(derive EOM using L = T − V;\nEuler-Lagrange applied)"),

    ("Q5(b)\n[5M]",
     "Newton vs Lagrange — Comparison\n(force-based vs energy-based;\nadvantages, limitations, pendulum example)",
     "Impulse-Momentum Theory\n(J = Δp, coefficient of restitution,\nconservation conditions)",
     "Normal Modes & Modal Analysis\n(eigenvalue problem in vibrations;\nω_n & mode shapes from [M] & [K])"),

    ("Q5(c)\n[5M]",
     "Frictionless Ramp + Rough Surface\n(energy conservation to find v_bottom;\nwork-energy to find stopping distance)",
     "Car Acceleration — Power & Energy\n(1200 kg, 20→40 m/s in 8 s;\nengine force, average & instantaneous power)",
     "Simple Pendulum Numerical\n(L=1.5 m, m=2 kg; Lagrangian, EOM,\nperiod; compare with physical pendulum)"),

    ("Q5(d)\n[5M]",
     "Ball-Bat Impulse Problem\n(impulse, average force;\nKE before/after; energy NOT conserved)",
     "Partially Elastic Collision — Numerical\n(e=0.5; velocities post-collision;\nimpulse, KE loss)",
     "Numerical ODE Solvers — RK4/Euler\n(Forward Euler, RK2, RK4;\naccuracy order, stability, why RK4)"),
]

Q6_TOPICS = [
    ("Q6(a)\n[10M]\n(FBD)",
     "Conveyor Belt Transfer — FBD\n(2 kg package, v₁=1.5→v₂=3.0 m/s;\nfriction, acceleration, heat dissipated)",
     "Mobile Manipulator on AGV — FBD\n(v_AGV=0.5 m/s, arm L=1.2 m, θ=30°;\ntip velocity, vibration isolator design)",
     "Rotating Sensor Array — FBD\n(ω=2 rad/s, sensor at r=0.5 m;\ncentripetal & Coriolis accels, constraint forces)"),

    ("Q6(b)\n[10M]\n(Numerical)",
     "Slider-Crank Mechanism\n(r=50 mm, L=150 mm, 3000 RPM, θ=30°;\nφ, piston position, piston velocity)",
     "CNC Trapezoidal Velocity Profile\n(200 mm & 15 mm moves;\nacceleration/deceleration times, total time)",
     "Rough Incline + Horizontal Surface\n(3 kg, 35°, μ_k=0.25 on incline;\nμ_k=0.3 on flat; total friction heat)"),
]

Q7_TOPICS = [
    ("Q7(a)\n[10M]\n(FBD)",
     "Yo-Yo Dynamics — FBD\n(m=50 g, R=30 mm, r=10 mm;\nacceleration, tension, angular acc., % rotational KE)",
     "Spring-Mass-Damper — Full Analysis\n(FBD + EOM classification;\nfree response x(t) with initial conditions)",
     "Conveyor Belt Transfer — FBD\n(2 kg package, dual-belt transfer;\nfriction forces, time, heat dissipated)"),

    ("Q7(b)\n[10M]\n(Numerical)",
     "2-DOF Mass-Spring System\n([M] & [K] matrices; eigenvalue equation;\ntwo natural frequencies & mode shapes)",
     "Double Pendulum\n(T & V expressions; Euler-Lagrange EOMs;\nsmall-angle linearisation; chaos comment)",
     "Compound Gear Train\n(2 stages; overall gear ratio;\noutput speed, torque, power verification)"),
]

ALL_TOPICS = [
    ("Q1 — Compulsory  (Answer ALL 4 parts · 5 marks each = 20 marks)", Q1_TOPICS),
    ("Q2 — Pure Numerical: Particle Kinetics / Constrained Motion  (20 marks)", Q2_TOPICS),
    ("Q3 — Pure Numerical: Rigid Body Dynamics & Vibrations  (20 marks)", Q3_TOPICS),
    ("Q4 — Theory (10M) + Numerical (10M): Kinematics / Rotating Frames  (20 marks)", Q4_TOPICS),
    ("Q5 — Theory (10M) + Numerical (10M): Energy Methods / Lagrangian  (20 marks)", Q5_TOPICS),
    ("Q6 — FBD (10M) + Difficult Numerical (10M)  (20 marks)", Q6_TOPICS),
    ("Q7 — FBD (10M) + Difficult Numerical (10M)  (20 marks)", Q7_TOPICS),
]

# ─── Colour palette ──────────────────────────────────────────────────────────
C_DARK   = colors.HexColor('#2c3e50')
C_BLUE   = colors.HexColor('#2980b9')
C_GREEN  = colors.HexColor('#27ae60')
C_ORANGE = colors.HexColor('#e67e22')
C_RED    = colors.HexColor('#c0392b')
C_LIGHT  = colors.HexColor('#ecf0f1')
C_A      = colors.HexColor('#d6eaf8')   # Set A column
C_B      = colors.HexColor('#d5f5e3')   # Set B column
C_C      = colors.HexColor('#fdebd0')   # Set C column
C_HEAD_A = colors.HexColor('#1a5276')
C_HEAD_B = colors.HexColor('#1e8449')
C_HEAD_C = colors.HexColor('#7d6608')

# ─────────────────────────────────────────────────────────────────────────────
#  PDF 1 — Topic Mapping (landscape A4)
# ─────────────────────────────────────────────────────────────────────────────

def build_topic_pdf():
    out = OUT_DIR / "DSM_Topic_Mapping.pdf"
    doc = SimpleDocTemplate(str(out), pagesize=landscape(A4),
                            topMargin=0.5*inch, bottomMargin=0.5*inch,
                            leftMargin=0.5*inch, rightMargin=0.5*inch)
    styles = getSampleStyleSheet()
    story  = []

    def h(text, size=14, color=C_DARK, space_before=12, space_after=6):
        s = ParagraphStyle('_h', parent=styles['Normal'], fontSize=size,
                           fontName='Helvetica-Bold', textColor=color,
                           spaceBefore=space_before, spaceAfter=space_after,
                           alignment=TA_CENTER)
        story.append(Paragraph(text, s))

    def para(text, size=9, align=TA_CENTER):
        s = ParagraphStyle('_p', parent=styles['Normal'], fontSize=size,
                           fontName='Helvetica', alignment=align, spaceAfter=3)
        story.append(Paragraph(text, s))

    # ── Title page header ──
    h("DSM — Question Paper Topic Mapping", size=16)
    h("Dynamic Systems Modeling (702MH0C025) · B.Tech Mechatronics Sem IV · AY 2025-26", size=10, color=C_BLUE)
    para("All three examination sets compared question-by-question · Prepared by Dr. Sunny Nanade, Course Instructor", size=9)
    story.append(HRFlowable(width="100%", thickness=1.5, color=C_DARK, spaceAfter=8))

    # ── Legend ──
    legend_data = [
        [Paragraph("<b>Set A</b>", _cs(8, C_HEAD_A)),
         Paragraph("<b>Set B</b>", _cs(8, C_HEAD_B)),
         Paragraph("<b>Set C</b>", _cs(8, C_HEAD_C)),
         Paragraph("Note: Q2–Q7 → Solve any FOUR (4×20 = 80 marks) · Q1 is Compulsory", _cs(8, C_DARK))]
    ]
    legend_t = Table(legend_data, colWidths=[1.2*inch, 1.2*inch, 1.2*inch, 6.4*inch])
    legend_t.setStyle(TableStyle([
        ('BACKGROUND', (0,0),(0,0), C_A),
        ('BACKGROUND', (1,0),(1,0), C_B),
        ('BACKGROUND', (2,0),(2,0), C_C),
        ('BOX',        (0,0),(-1,-1), 0.8, C_DARK),
        ('ALIGN',      (0,0),(-1,-1), 'CENTER'),
        ('VALIGN',     (0,0),(-1,-1), 'MIDDLE'),
        ('PADDING',    (0,0),(-1,-1), 5),
    ]))
    story.append(legend_t)
    story.append(Spacer(1, 10))

    # ── Section tables ──
    for section_title, rows in ALL_TOPICS:
        story.append(Spacer(1, 6))
        sec_style = ParagraphStyle('_sec', parent=styles['Normal'], fontSize=9.5,
                                   fontName='Helvetica-Bold', textColor=colors.white,
                                   backColor=C_DARK, borderPadding=5,
                                   alignment=TA_LEFT, spaceBefore=4, spaceAfter=3)
        story.append(Paragraph(f"  {section_title}", sec_style))

        # Header row
        tbl_data = [[
            Paragraph("<b>Q. No.</b>",    _cs(8, colors.white)),
            Paragraph("<b>SET A</b>",     _cs(8, colors.white)),
            Paragraph("<b>SET B</b>",     _cs(8, colors.white)),
            Paragraph("<b>SET C</b>",     _cs(8, colors.white)),
        ]]

        for q_label, topic_a, topic_b, topic_c in rows:
            tbl_data.append([
                Paragraph(q_label,   _cs(8.5, C_DARK, bold=True)),
                Paragraph(topic_a,   _cs(8.5, C_HEAD_A)),
                Paragraph(topic_b,   _cs(8.5, C_HEAD_B)),
                Paragraph(topic_c,   _cs(8.5, C_HEAD_C)),
            ])

        # Q6 & Q7 have 2 sub-rows (a and b), others have 4
        col_w = [0.75*inch, 3.15*inch, 3.15*inch, 3.15*inch]
        tbl = Table(tbl_data, colWidths=col_w, repeatRows=1)

        row_styles = [
            ('BACKGROUND', (0,0), (-1,0), C_DARK),
            ('TEXTCOLOR',  (0,0), (-1,0), colors.white),
            ('FONTNAME',   (0,0), (-1,0), 'Helvetica-Bold'),
            ('GRID',       (0,0), (-1,-1), 0.5, colors.grey),
            ('VALIGN',     (0,0), (-1,-1), 'MIDDLE'),
            ('ALIGN',      (0,0), (0,-1),  'CENTER'),
            ('ALIGN',      (1,0), (3,-1),  'LEFT'),
            ('PADDING',    (0,0), (-1,-1), 5),
        ]
        # Alternate row colours per column
        for ri in range(1, len(tbl_data)):
            row_styles.append(('BACKGROUND', (1, ri), (1, ri), C_A))
            row_styles.append(('BACKGROUND', (2, ri), (2, ri), C_B))
            row_styles.append(('BACKGROUND', (3, ri), (3, ri), C_C))
        tbl.setStyle(TableStyle(row_styles))
        story.append(tbl)

    story.append(Spacer(1, 12))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.grey))
    para("QBMS Format ≡ Final QP content (identical questions, different layout). "
         "Synoptic Table is identical across all 3 sets — same CO/BL/Unit coverage. "
         "Dr. Sunny Nanade, Course Instructor · NMIMS STME Indore", size=8)

    doc.build(story)
    print(f"✅  Topic Mapping PDF → {out}")


# ─────────────────────────────────────────────────────────────────────────────
#  PDF 2 — Student Exam Template (portrait A4)
# ─────────────────────────────────────────────────────────────────────────────

UNIT_NAMES = {
    "1": "Unit 1: Kinematics of Particles",
    "2": "Unit 2: Kinetics of Particles — Newton's Laws",
    "3": "Unit 3: Kinematics of Rigid Bodies",
    "4": "Unit 4: Kinetics of Rigid Bodies",
    "5": "Unit 5: Energy & Momentum Methods",
    "6": "Unit 6: Vibrations & Oscillations",
}

CO_DESCS = {
    "CO1": "Understand & apply kinematics of particles and rigid bodies",
    "CO2": "Analyse dynamic systems using Free Body Diagrams",
    "CO3": "Calculate forces acting on dynamic systems",
    "CO4": "Apply constitutive laws to dynamic systems",
    "CO5": "Calculate energy, work, and power in dynamic systems",
}

BL_DESCS = {
    "L1": "Remember",
    "L2": "Understand",
    "L3": "Apply",
    "L4": "Analyse",
    "L5": "Evaluate",
}

MARKING_SCHEME = [
    # (Q.No, Description, Unit(s), CO, BL, Marks, Type, Difficulty)
    ("Q1",    "Compulsory — Attempt ALL 4 sub-parts",         "1–6", "CO1–CO5", "L2–L3", 20,  "Mixed",       "Easy–Medium"),
    ("Q1(a)", "Theory: Definitions / Core Concepts",          "1, 3", "CO1",    "L2",     5,  "Theory",      "Easy"),
    ("Q1(b)", "Numerical: Particle Kinematics",               "1",    "CO1",    "L3",     5,  "Numerical",   "Easy"),
    ("Q1(c)", "Numerical: Constrained Motion / Pulleys",      "4",    "CO3",    "L3",     5,  "Numerical",   "Medium"),
    ("Q1(d)", "Numerical: Energy / Rigid Body",               "5, 6", "CO5",    "L3",     5,  "Numerical",   "Medium"),
    ("─"*5,   "─"*30, "─"*6, "─"*8, "─"*4, "─", "─"*10, "─"*12),
    ("Q2",    "Pure Numerical: Particle Kinetics (4 parts × 5M)",    "4",    "CO3, CO4", "L3", 20, "Numerical",  "Medium"),
    ("Q3",    "Pure Numerical: Rigid Body & Vibrations (4 parts × 5M)", "5",  "CO4, CO5", "L3", 20, "Numerical",  "Medium"),
    ("Q4",    "Theory (10M) + Numerical (10M): Kinematics / Rotating Frames",  "3",    "CO1, CO3", "L4", 20, "Theory+Num", "Medium"),
    ("Q5",    "Theory (10M) + Numerical (10M): Energy Methods / Lagrangian",   "2, 6", "CO4, CO5", "L4", 20, "Theory+Num", "Hard"),
    ("Q6",    "FBD (10M) + Difficult Numerical (10M): Applied Dynamics",       "4, 5", "CO2, CO3", "L5", 20, "FBD+Num",    "Hard"),
    ("Q7",    "FBD (10M) + Difficult Numerical (10M): Advanced Systems",       "5, 6", "CO2, CO5", "L5", 20, "FBD+Num",    "Hard"),
]


def build_template_pdf():
    out = OUT_DIR / "DSM_Student_Template.pdf"
    doc = SimpleDocTemplate(str(out), pagesize=A4,
                            topMargin=0.65*inch, bottomMargin=0.65*inch,
                            leftMargin=0.75*inch, rightMargin=0.75*inch)
    styles = getSampleStyleSheet()
    story  = []

    # ── University Header ──
    def ctr(text, size=11, bold=True, color=C_DARK, space_after=3):
        s = ParagraphStyle('_c', parent=styles['Normal'], fontSize=size,
                           fontName='Helvetica-Bold' if bold else 'Helvetica',
                           textColor=color, alignment=TA_CENTER, spaceAfter=space_after)
        story.append(Paragraph(text, s))

    ctr("SVKM's NMIMS (Deemed-to-be University)", 13)
    ctr("School of Technology Management & Engineering (STME), Indore", 10)
    ctr("TERM END EXAMINATION — MARCH 2026", 10)
    ctr("Dynamic Systems Modeling (702MH0C025)", 12, color=C_BLUE)
    story.append(HRFlowable(width="100%", thickness=1.5, color=C_DARK, spaceAfter=5))

    # ── Course info row ──
    info_data = [["Program: B.Tech Mechatronics", "Semester: IV",
                  "Duration: 3 Hours", "Maximum Marks: 100"]]
    info_t = Table(info_data, colWidths=[1.8*inch, 1.1*inch, 1.3*inch, 1.8*inch])
    info_t.setStyle(TableStyle([
        ('FONTNAME',  (0,0),(-1,-1), 'Helvetica'),
        ('FONTSIZE',  (0,0),(-1,-1), 9),
        ('ALIGN',     (0,0),(-1,-1), 'CENTER'),
        ('BACKGROUND',(0,0),(-1,-1), C_LIGHT),
        ('BOX',       (0,0),(-1,-1), 0.8, C_DARK),
        ('INNERGRID', (0,0),(-1,-1), 0.5, colors.grey),
        ('PADDING',   (0,0),(-1,-1), 5),
    ]))
    story.append(info_t)
    story.append(Spacer(1, 8))

    # ── Instructions ──
    inst_style = ParagraphStyle('_inst', parent=styles['Normal'], fontSize=9,
                                fontName='Helvetica', alignment=TA_JUSTIFY,
                                spaceAfter=8, backColor=colors.Color(1,1,0.85),
                                borderColor=C_ORANGE, borderWidth=1, borderPadding=6)
    story.append(Paragraph(
        "<b>Instructions to Students:</b><br/>"
        "1. <b>Q1 is compulsory</b> (20 marks) — attempt all four sub-parts.<br/>"
        "2. From Q2 to Q7, <b>attempt any FOUR</b> questions (4 × 20 = 80 marks).<br/>"
        "3. Draw neat <b>Free Body Diagrams</b> wherever applicable.<br/>"
        "4. No programmable calculators. Use <b>g = 9.81 m/s²</b> unless stated otherwise.<br/>"
        "5. All numerical answers must include <b>proper units</b>.<br/>"
        "6. Q4 &amp; Q5 contain both a <b>theory (10M)</b> and a <b>numerical (10M)</b> part.<br/>"
        "7. Q6 &amp; Q7 contain an <b>FBD analysis (10M)</b> and a <b>difficult numerical (10M)</b>.",
        inst_style))

    # ── Marking Scheme table ──
    story.append(Paragraph("<b>Marking Scheme &amp; Syllabus Coverage</b>",
                            ParagraphStyle('_mh', parent=styles['Normal'], fontSize=11,
                                           fontName='Helvetica-Bold', textColor=colors.white,
                                           backColor=C_DARK, borderPadding=5,
                                           alignment=TA_CENTER, spaceAfter=4)))

    ms_header = [
        Paragraph("<b>Q. No.</b>",    _cs(8, colors.white)),
        Paragraph("<b>Description</b>", _cs(8, colors.white)),
        Paragraph("<b>Unit(s)</b>",   _cs(8, colors.white)),
        Paragraph("<b>CO</b>",        _cs(8, colors.white)),
        Paragraph("<b>Bloom's</b>",   _cs(8, colors.white)),
        Paragraph("<b>Marks</b>",     _cs(8, colors.white)),
        Paragraph("<b>Type</b>",      _cs(8, colors.white)),
        Paragraph("<b>Difficulty</b>",_cs(8, colors.white)),
    ]
    ms_data = [ms_header]

    for row in MARKING_SCHEME:
        q, desc, units, co, bl, marks, qtype, diff = row
        if "─" in str(q):
            ms_data.append([Paragraph("─"*3, _cs(7, colors.grey))]*8)
            continue
        # colour difficulty
        diff_color = (C_GREEN if "Easy" in str(diff) else
                      C_ORANGE if "Medium" in str(diff) else C_RED)
        ms_data.append([
            Paragraph(str(q),     _cs(8.5, C_DARK, bold=True)),
            Paragraph(str(desc),  _cs(8.5, C_DARK)),
            Paragraph(str(units), _cs(8.5, C_BLUE, bold=True)),
            Paragraph(str(co),    _cs(8.5, C_DARK, bold=True)),
            Paragraph(str(bl),    _cs(8.5, C_DARK)),
            Paragraph(str(marks), _cs(9, C_RED, bold=True)),
            Paragraph(str(qtype), _cs(8, C_DARK)),
            Paragraph(str(diff),  _cs(8.5, diff_color, bold=True)),
        ])

    ms_t = Table(ms_data,
                 colWidths=[0.65*inch, 2.55*inch, 0.65*inch,
                            0.75*inch, 0.65*inch, 0.5*inch,
                            0.9*inch,  0.8*inch],
                 repeatRows=1)
    ms_styles = [
        ('BACKGROUND', (0,0), (-1,0),  C_DARK),
        ('TEXTCOLOR',  (0,0), (-1,0),  colors.white),
        ('GRID',       (0,0), (-1,-1), 0.5, colors.grey),
        ('ALIGN',      (0,0), (-1,-1), 'CENTER'),
        ('VALIGN',     (0,0), (-1,-1), 'MIDDLE'),
        ('PADDING',    (0,0), (-1,-1), 4),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, C_LIGHT]),
    ]
    # Highlight Q1 block
    for ri in range(1, 6):
        ms_styles.append(('BACKGROUND', (0,ri), (-1,ri), colors.Color(0.9, 0.93, 1.0)))
    ms_t.setStyle(TableStyle(ms_styles))
    story.append(ms_t)
    story.append(Spacer(1, 10))

    # ── Marks Split ──
    story.append(Paragraph("<b>Marks Distribution</b>",
                            ParagraphStyle('_mh2', parent=styles['Normal'], fontSize=10,
                                           fontName='Helvetica-Bold', textColor=C_DARK,
                                           spaceAfter=4)))
    marks_data = [
        [Paragraph("<b>Section</b>", _cs(9, colors.white)),
         Paragraph("<b>Questions</b>", _cs(9, colors.white)),
         Paragraph("<b>Marks per Q</b>", _cs(9, colors.white)),
         Paragraph("<b>Total Marks</b>", _cs(9, colors.white))],
        ["Q1 — Compulsory", "Q1(a) + Q1(b) + Q1(c) + Q1(d)", "5 marks each", "20 marks"],
        ["Q2–Q7 — Elective", "Attempt any FOUR from Q2, Q3, Q4, Q5, Q6, Q7", "20 marks each", "80 marks"],
        [Paragraph("<b>Grand Total</b>", _cs(9, C_DARK, bold=True)),
         "",
         "",
         Paragraph("<b>100 marks</b>", _cs(10, C_RED, bold=True))],
    ]
    marks_t = Table(marks_data, colWidths=[1.4*inch, 3.2*inch, 1.1*inch, 1.1*inch])
    marks_t.setStyle(TableStyle([
        ('BACKGROUND',  (0,0), (-1,0), C_DARK),
        ('TEXTCOLOR',   (0,0), (-1,0), colors.white),
        ('BACKGROUND',  (0,3), (-1,3), colors.Color(1, 0.95, 0.85)),
        ('GRID',        (0,0), (-1,-1), 0.8, colors.grey),
        ('ALIGN',       (0,0), (-1,-1), 'CENTER'),
        ('VALIGN',      (0,0), (-1,-1), 'MIDDLE'),
        ('PADDING',     (0,0), (-1,-1), 6),
        ('FONTSIZE',    (0,1), (-1,-1), 9),
        ('ROWBACKGROUNDS', (0,1), (-1,2), [colors.white, C_LIGHT]),
    ]))
    story.append(marks_t)
    story.append(Spacer(1, 10))

    # ── CO Table ──
    story.append(Paragraph("<b>Course Outcomes (COs) Assessed</b>",
                            ParagraphStyle('_coh', parent=styles['Normal'], fontSize=10,
                                           fontName='Helvetica-Bold', textColor=C_DARK,
                                           spaceAfter=4)))
    co_data = [[Paragraph("<b>CO</b>", _cs(9, colors.white)),
                Paragraph("<b>Description</b>", _cs(9, colors.white)),
                Paragraph("<b>Questions</b>", _cs(9, colors.white))]]
    co_qs = {
        "CO1": "Q1(a), Q1(b), Q4",
        "CO2": "Q6(a), Q7(a) [FBD]",
        "CO3": "Q1(c), Q2, Q4, Q6",
        "CO4": "Q1(d), Q2, Q3, Q5",
        "CO5": "Q1(d), Q3, Q5, Q7",
    }
    for co, desc in CO_DESCS.items():
        co_data.append([
            Paragraph(co, _cs(9, C_DARK, bold=True)),
            Paragraph(desc, _cs(9, C_DARK)),
            Paragraph(co_qs.get(co, "—"), _cs(9, C_BLUE)),
        ])
    co_t = Table(co_data, colWidths=[0.65*inch, 4.2*inch, 1.9*inch])
    co_t.setStyle(TableStyle([
        ('BACKGROUND',  (0,0), (-1,0), C_DARK),
        ('TEXTCOLOR',   (0,0), (-1,0), colors.white),
        ('GRID',        (0,0), (-1,-1), 0.5, colors.grey),
        ('ALIGN',       (0,0), (0,-1), 'CENTER'),
        ('ALIGN',       (1,0), (-1,-1), 'LEFT'),
        ('VALIGN',      (0,0), (-1,-1), 'MIDDLE'),
        ('PADDING',     (0,0), (-1,-1), 5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, C_LIGHT]),
    ]))
    story.append(co_t)
    story.append(Spacer(1, 10))

    # ── Unit coverage ──
    story.append(Paragraph("<b>Syllabus Units Covered</b>",
                            ParagraphStyle('_uh', parent=styles['Normal'], fontSize=10,
                                           fontName='Helvetica-Bold', textColor=C_DARK,
                                           spaceAfter=4)))
    unit_cov = {
        "1": "Q1(b) — particle kinematics",
        "2": "Q5 — Newton's laws, work-energy",
        "3": "Q1(a), Q4 — kinematics of rigid bodies, rotating frames",
        "4": "Q1(c), Q2, Q6 — kinetics, constrained motion, FBD",
        "5": "Q1(d), Q3, Q5, Q6, Q7 — energy/momentum, vibrations, rolling",
        "6": "Q1(d), Q3, Q5, Q7 — vibrations, Lagrangian methods",
    }
    unit_data = [[Paragraph("<b>Unit</b>", _cs(9, colors.white)),
                  Paragraph("<b>Title</b>", _cs(9, colors.white)),
                  Paragraph("<b>Relevant Questions</b>", _cs(9, colors.white))]]
    for u, title in UNIT_NAMES.items():
        unit_data.append([
            Paragraph(f"Unit {u}", _cs(9, C_DARK, bold=True)),
            Paragraph(title.split(": ", 1)[1], _cs(9, C_DARK)),
            Paragraph(unit_cov.get(u, "—"), _cs(9, C_BLUE)),
        ])
    unit_t = Table(unit_data, colWidths=[0.65*inch, 2.6*inch, 3.5*inch])
    unit_t.setStyle(TableStyle([
        ('BACKGROUND',  (0,0), (-1,0), C_DARK),
        ('TEXTCOLOR',   (0,0), (-1,0), colors.white),
        ('GRID',        (0,0), (-1,-1), 0.5, colors.grey),
        ('ALIGN',       (0,0), (0,-1), 'CENTER'),
        ('ALIGN',       (1,0), (-1,-1), 'LEFT'),
        ('VALIGN',      (0,0), (-1,-1), 'MIDDLE'),
        ('PADDING',     (0,0), (-1,-1), 5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, C_LIGHT]),
    ]))
    story.append(unit_t)
    story.append(Spacer(1, 10))

    # ── Preparation tips ──
    tips_style = ParagraphStyle('_tips', parent=styles['Normal'], fontSize=8.5,
                                fontName='Helvetica', alignment=TA_JUSTIFY,
                                spaceAfter=3, leftIndent=6)
    story.append(Paragraph("<b>Preparation Tips</b>",
                            ParagraphStyle('_th', parent=styles['Normal'], fontSize=10,
                                           fontName='Helvetica-Bold', textColor=C_DARK,
                                           spaceAfter=4)))
    tips = [
        "• <b>Q1 (compulsory):</b> Revise all definitions and short numerical from all units. Easy marks!",
        "• <b>Q2 (Particle Kinetics):</b> Pulleys, inclined planes, circular motion. Practice F = ma applications.",
        "• <b>Q3 (Rigid Body & Vibrations):</b> Rolling objects, pendulums, spring-mass-damper — know formulas cold.",
        "• <b>Q4 (Kinematics/Rotating Frames):</b> Derive velocity and acceleration equations. Know Coriolis.",
        "• <b>Q5 (Energy/Lagrangian):</b> Practise Lagrange formulation and work-energy theorem problems.",
        "• <b>Q6 &amp; Q7 (FBD + Difficult Numerical):</b> Always draw FBD first — it's worth 10 marks on its own!",
        "• <b>Recommended strategy:</b> Attempt Q1 → then pick 4 from Q2–Q7 based on your strongest units.",
    ]
    for tip in tips:
        story.append(Paragraph(tip, tips_style))
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.grey, spaceAfter=4))
    story.append(Paragraph(
        "This template is provided for preparation purposes only. Exact question numbers and specific numerical "
        "values will differ in the actual examination paper. Good luck! — Dr. Sunny Nanade, Course Instructor",
        ParagraphStyle('_foot', parent=styles['Normal'], fontSize=8,
                       fontName='Helvetica', textColor=colors.grey,
                       alignment=TA_CENTER)))

    doc.build(story)
    print(f"✅  Student Template PDF → {out}")


# ─── Helper: paragraph style shortcut ────────────────────────────────────────
def _cs(size, color=colors.black, bold=False):
    return ParagraphStyle('_x', fontName='Helvetica-Bold' if bold else 'Helvetica',
                          fontSize=size, textColor=color, leading=size*1.3,
                          spaceAfter=1)


if __name__ == "__main__":
    print("Building DSM exam documentation PDFs...")
    build_topic_pdf()
    build_template_pdf()
    print("\nDone! Files saved in:", OUT_DIR)
