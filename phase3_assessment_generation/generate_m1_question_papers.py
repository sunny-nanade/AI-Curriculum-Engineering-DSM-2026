"""
Dynamic Systems Modeling - Question Paper Generator
Generates 10 sets of question papers for the exam

Exam Details:
- Date: 19-02-2026
- Duration: 45 minutes
- Total Marks: 10
- Pattern: Q1 compulsory (4 marks), Solve any 2 from Q2/Q3/Q4 (6 marks)
"""

import random
from datetime import datetime
from pathlib import Path
import math

# Try to import reportlab, if not available will use HTML
try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False
    print("⚠️  ReportLab not available. Will generate HTML files instead.")
    print("   Install with: pip install reportlab")


class QuestionPaperGenerator:
    """Generates question papers with varying difficulty and parameters"""
    
    def __init__(self):
        self.exam_date = "19-02-2026"
        self.duration = "45 minutes"
        self.total_marks = 10
        self.institution = "Mukesh Patel School of Technology Management & Engineering"
        self.course = "Dynamic Systems Modeling (702MH0C023)"
        self.program = "B.Tech Mechatronics Engineering, Semester IV"
        
    def generate_all_sets(self, num_sets=10):
        """Generate all question paper sets"""
        output_dir = Path("question_papers")
        output_dir.mkdir(exist_ok=True)
        
        for set_num in range(1, num_sets + 1):
            print(f"Generating Set {set_num}...")
            
            if REPORTLAB_AVAILABLE:
                self.generate_pdf_set(set_num, output_dir)
            else:
                self.generate_html_set(set_num, output_dir)
        
        print(f"\n✅ Successfully generated {num_sets} question paper sets!")
        print(f"📁 Location: {output_dir.absolute()}")
    
    def generate_pdf_set(self, set_num, output_dir):
        """Generate PDF question paper using ReportLab"""
        filename = output_dir / f"DSM_Question_Paper_Set_{set_num:02d}.pdf"
        doc = SimpleDocTemplate(str(filename), pagesize=A4,
                               topMargin=0.5*inch, bottomMargin=0.5*inch,
                               leftMargin=0.75*inch, rightMargin=0.75*inch)
        
        story = []
        styles = getSampleStyleSheet()
        
        # Custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=14,
            textColor=colors.HexColor('#1a1a1a'),
            spaceAfter=6,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        )
        
        subtitle_style = ParagraphStyle(
            'CustomSubtitle',
            parent=styles['Normal'],
            fontSize=10,
            textColor=colors.HexColor('#333333'),
            spaceAfter=4,
            alignment=TA_CENTER,
            fontName='Helvetica'
        )
        
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=11,
            textColor=colors.HexColor('#000000'),
            spaceAfter=6,
            spaceBefore=6,
            fontName='Helvetica-Bold'
        )
        
        question_style = ParagraphStyle(
            'QuestionStyle',
            parent=styles['Normal'],
            fontSize=10,
            textColor=colors.HexColor('#000000'),
            spaceAfter=4,
            spaceBefore=4,
            fontName='Helvetica',
            leading=14
        )
        
        # Header
        story.append(Paragraph(self.institution, title_style))
        story.append(Paragraph(self.course, subtitle_style))
        story.append(Paragraph(self.program, subtitle_style))
        story.append(Spacer(1, 0.15*inch))
        
        # Exam info table
        exam_info = [
            ['Date:', self.exam_date, 'Duration:', self.duration],
            ['Total Marks:', str(self.total_marks), 'Set Number:', f'{set_num} of 10']
        ]
        
        exam_table = Table(exam_info, colWidths=[1.2*inch, 1.8*inch, 1.2*inch, 1.8*inch])
        exam_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f0f0f0')),
            ('BACKGROUND', (2, 0), (2, -1), colors.HexColor('#f0f0f0')),
        ]))
        story.append(exam_table)
        story.append(Spacer(1, 0.15*inch))
        
        # Instructions
        instructions = """
        <b>Instructions:</b><br/>
        1. Q1 is compulsory (4 marks).<br/>
        2. Solve ANY TWO from Q2, Q3, and Q4 (3 marks each = 6 marks).<br/>
        3. Use of non-programmable calculators is permitted.<br/>
        4. All answers should include proper units and significant figures.
        """
        story.append(Paragraph(instructions, question_style))
        story.append(Spacer(1, 0.1*inch))
        
        # Generate questions for this set
        questions = self.generate_questions_for_set(set_num)
        
        # Q1 - Compulsory
        story.append(Paragraph("<b>Q1. Answer the following (Compulsory):</b> [4 Marks]", heading_style))
        
        # Q1(a)
        story.append(Paragraph("<b>(a)</b> " + questions['q1a']['question'] + " [2 Marks]", question_style))
        for i, subq in enumerate(questions['q1a']['subquestions'], 1):
            story.append(Paragraph(f"&nbsp;&nbsp;&nbsp;&nbsp;({chr(96+i)}) {subq} <i>[0.5]</i>", question_style))
        story.append(Spacer(1, 0.1*inch))
        
        # Q1(b)
        story.append(Paragraph("<b>(b)</b> " + questions['q1b']['question'] + " [2 Marks]", question_style))
        for i, subq in enumerate(questions['q1b']['subquestions'], 1):
            story.append(Paragraph(f"&nbsp;&nbsp;&nbsp;&nbsp;({chr(96+i)}) {subq} <i>[0.5]</i>", question_style))
        story.append(Spacer(1, 0.15*inch))
        
        # Q2, Q3, Q4 - Solve any two
        story.append(Paragraph("<b>Solve ANY TWO from the following:</b> [3 Marks each = 6 Marks]", heading_style))
        
        # Q2
        story.append(Paragraph("<b>Q2.</b> " + questions['q2']['question'] + " [3 Marks]", question_style))
        for i, subq in enumerate(questions['q2']['subquestions'], 1):
            story.append(Paragraph(f"&nbsp;&nbsp;&nbsp;&nbsp;({chr(96+i)}) {subq} <i>[0.5]</i>", question_style))
        story.append(Spacer(1, 0.1*inch))
        
        # Q3
        story.append(Paragraph("<b>Q3.</b> " + questions['q3']['question'] + " [3 Marks]", question_style))
        for i, subq in enumerate(questions['q3']['subquestions'], 1):
            story.append(Paragraph(f"&nbsp;&nbsp;&nbsp;&nbsp;({chr(96+i)}) {subq} <i>[0.5]</i>", question_style))
        story.append(Spacer(1, 0.1*inch))
        
        # Q4
        story.append(Paragraph("<b>Q4.</b> " + questions['q4']['question'] + " [3 Marks]", question_style))
        for i, subq in enumerate(questions['q4']['subquestions'], 1):
            story.append(Paragraph(f"&nbsp;&nbsp;&nbsp;&nbsp;({chr(96+i)}) {subq} <i>[0.5]</i>", question_style))
        
        # Build PDF
        doc.build(story)
    
    def generate_html_set(self, set_num, output_dir):
        """Generate HTML question paper (fallback when ReportLab not available)"""
        filename = output_dir / f"DSM_Question_Paper_Set_{set_num:02d}.html"
        
        questions = self.generate_questions_for_set(set_num)
        
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>DSM Question Paper - Set {set_num}</title>
    <style>
        @media print {{
            @page {{ margin: 0.5in; }}
        }}
        body {{
            font-family: 'Times New Roman', Times, serif;
            max-width: 8.5in;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
        }}
        .header {{
            text-align: center;
            margin-bottom: 20px;
        }}
        .header h1 {{
            font-size: 16px;
            margin: 5px 0;
        }}
        .header h2 {{
            font-size: 12px;
            font-weight: normal;
            margin: 3px 0;
        }}
        .exam-info {{
            border: 1px solid #333;
            padding: 10px;
            margin: 15px 0;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
            font-size: 11px;
        }}
        .exam-info strong {{
            display: inline-block;
            width: 120px;
        }}
        .instructions {{
            margin: 15px 0;
            padding: 10px;
            background: #f5f5f5;
            border-left: 3px solid #333;
            font-size: 11px;
        }}
        .question-section {{
            margin: 15px 0;
        }}
        .question-header {{
            font-weight: bold;
            font-size: 12px;
            margin: 10px 0 5px 0;
        }}
        .question {{
            margin: 8px 0;
            font-size: 11px;
        }}
        .subquestion {{
            margin-left: 30px;
            margin-top: 4px;
            font-size: 11px;
        }}
        .marks {{
            color: #666;
            font-style: italic;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{self.institution}</h1>
        <h2>{self.course}</h2>
        <h2>{self.program}</h2>
    </div>
    
    <div class="exam-info">
        <div><strong>Date:</strong> {self.exam_date}</div>
        <div><strong>Duration:</strong> {self.duration}</div>
        <div><strong>Total Marks:</strong> {self.total_marks}</div>
        <div><strong>Set Number:</strong> {set_num} of 10</div>
    </div>
    
    <div class="instructions">
        <strong>Instructions:</strong>
        <ol style="margin: 5px 0; padding-left: 20px;">
            <li>Q1 is compulsory (4 marks).</li>
            <li>Solve ANY TWO from Q2, Q3, and Q4 (3 marks each = 6 marks).</li>
            <li>Use of non-programmable calculators is permitted.</li>
            <li>All answers should include proper units and significant figures.</li>
        </ol>
    </div>
    
    <div class="question-section">
        <div class="question-header">Q1. Answer the following (Compulsory): [4 Marks]</div>
        
        <div class="question">
            <strong>(a)</strong> {questions['q1a']['question']} [2 Marks]
        </div>
"""
        
        for i, subq in enumerate(questions['q1a']['subquestions'], 1):
            html_content += f'        <div class="subquestion">({chr(96+i)}) {subq} <span class="marks">[0.5]</span></div>\n'
        
        html_content += f"""
        <div class="question" style="margin-top: 10px;">
            <strong>(b)</strong> {questions['q1b']['question']} [2 Marks]
        </div>
"""
        
        for i, subq in enumerate(questions['q1b']['subquestions'], 1):
            html_content += f'        <div class="subquestion">({chr(96+i)}) {subq} <span class="marks">[0.5]</span></div>\n'
        
        html_content += """
    </div>
    
    <div class="question-section">
        <div class="question-header">Solve ANY TWO from the following: [3 Marks each = 6 Marks]</div>
        
"""
        
        # Q2
        html_content += f'        <div class="question"><strong>Q2.</strong> {questions["q2"]["question"]} [3 Marks]</div>\n'
        for i, subq in enumerate(questions['q2']['subquestions'], 1):
            html_content += f'        <div class="subquestion">({chr(96+i)}) {subq} <span class="marks">[0.5]</span></div>\n'
        
        # Q3
        html_content += f'\n        <div class="question" style="margin-top: 10px;"><strong>Q3.</strong> {questions["q3"]["question"]} [3 Marks]</div>\n'
        for i, subq in enumerate(questions['q3']['subquestions'], 1):
            html_content += f'        <div class="subquestion">({chr(96+i)}) {subq} <span class="marks">[0.5]</span></div>\n'
        
        # Q4
        html_content += f'\n        <div class="question" style="margin-top: 10px;"><strong>Q4.</strong> {questions["q4"]["question"]} [3 Marks]</div>\n'
        for i, subq in enumerate(questions['q4']['subquestions'], 1):
            html_content += f'        <div class="subquestion">({chr(96+i)}) {subq} <span class="marks">[0.5]</span></div>\n'
        
        html_content += """
    </div>
</body>
</html>
"""
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
    
    def generate_questions_for_set(self, set_num):
        """Generate questions for a specific set number"""
        random.seed(set_num * 42)  # Reproducible randomization
        
        return {
            'q1a': self.generate_q1a(set_num),
            'q1b': self.generate_q1b(set_num),
            'q2': self.generate_q2(set_num),
            'q3': self.generate_q3(set_num),
            'q4': self.generate_q4(set_num)
        }
    
    def generate_q1a(self, set_num):
        """Q1(a) - Pure Theory (Easy) - 4 subquestions of 0.5 marks each"""
        
        theory_banks = [
            # Set 1-2: Basic definitions
            {
                'question': 'Answer the following theory questions:',
                'subquestions': [
                    'Define kinematics and kinetics.',
                    'State Newton\'s second law of motion for a particle.',
                    'What is an inertial reference frame?',
                    'Distinguish between position vector and displacement.'
                ]
            },
            {
                'question': 'Answer the following theory questions:',
                'subquestions': [
                    'Define velocity in terms of position vector.',
                    'What is the difference between speed and velocity?',
                    'State the relationship between linear and angular velocity for circular motion.',
                    'What is meant by absolute motion and relative motion?'
                ]
            },
            # Set 3-4: Coordinate systems
            {
                'question': 'Answer the following theory questions:',
                'subquestions': [
                    'List four coordinate systems used in dynamics.',
                    'Write the unit vectors for polar coordinates.',
                    'In which situations is cylindrical coordinate system preferred?',
                    'Define azimuthal angle in spherical coordinates.'
                ]
            },
            {
                'question': 'Answer the following theory questions:',
                'subquestions': [
                    'Write the transformation formula from Cartesian to polar coordinates.',
                    'What is the radial distance in spherical coordinates?',
                    'Define the base vectors in cylindrical coordinate system.',
                    'When would you use spherical coordinates instead of Cartesian?'
                ]
            },
            # Set 5-6: Newton's laws and forces
            {
                'question': 'Answer the following theory questions:',
                'subquestions': [
                    'State Newton\'s first law with an example.',
                    'What are constraint forces? Give one example.',
                    'Define normal force on an inclined plane.',
                    'Write the formula for kinetic friction force.'
                ]
            },
            {
                'question': 'Answer the following theory questions:',
                'subquestions': [
                    'What is the difference between static and kinetic friction?',
                    'Define free body diagram and its importance.',
                    'Write the equation of motion for a mass-spring system.',
                    'What is meant by conservative force?'
                ]
            },
            # Set 7-8: Lagrangian mechanics
            {
                'question': 'Answer the following theory questions:',
                'subquestions': [
                    'Define generalized coordinates with an example.',
                    'Write the expression for Lagrangian L in terms of kinetic and potential energy.',
                    'State the Euler-Lagrange equation.',
                    'What is a degree of freedom? Give an example.'
                ]
            },
            {
                'question': 'Answer the following theory questions:',
                'subquestions': [
                    'What are the advantages of Lagrangian formulation over Newtonian?',
                    'Define holonomic constraints.',
                    'Write the formula for kinetic energy of a particle.',
                    'What is gravitational potential energy for a mass near Earth\'s surface?'
                ]
            },
            # Set 9-10: Rigid bodies and rotation
            {
                'question': 'Answer the following theory questions:',
                'subquestions': [
                    'Define rigid body motion.',
                    'What is angular velocity vector?',
                    'Write the formula relating linear velocity to angular velocity: v = ?',
                    'Define pure rolling condition.'
                ]
            },
            {
                'question': 'Answer the following theory questions:',
                'subquestions': [
                    'What is the no-slip condition for a rolling wheel?',
                    'Define centripetal acceleration.',
                    'Write the relationship between angular acceleration alpha and linear acceleration a for circular motion.',
                    'What is meant by fixed frame and rotating frame?'
                ]
            }
        ]
        
        return theory_banks[set_num - 1]
    
    def generate_q1b(self, set_num):
        """Q1(b) - Theory + Numerical (Medium) - 4 subquestions of 0.5 marks each"""
        
        mixed_banks = [
            # Set 1
            {
                'question': 'Consider a particle moving with position vector r_vec(t) = (3t^2)i + (4t)j meters.',
                'subquestions': [
                    'Write the expression for velocity vector v_vec(t).',
                    'Calculate the speed at t = 2 seconds.',
                    'What physical quantity does dr_vec/dt represent?',
                    'Find the magnitude of velocity at t = 1 second.'
                ]
            },
            # Set 2
            {
                'question': 'A mass-spring system has m = 2 kg and k = 50 N/m.',
                'subquestions': [
                    'Define natural frequency omega_n.',
                    'Calculate omega_n for this system.',
                    'What is the period of oscillation T?',
                    'Write the equation of motion for this system.'
                ]
            },
            # Set 3
            {
                'question': 'A particle has Cartesian coordinates (3, 4) meters.',
                'subquestions': [
                    'Define radial coordinate r in polar system.',
                    'Calculate r for this particle.',
                    'Find the angle theta in radians.',
                    'What is theta in degrees?'
                ]
            },
            # Set 4
            {
                'question': 'Consider circular motion with radius R = 5 m and angular velocity omega = 2 rad/s.',
                'subquestions': [
                    'Write the formula for linear speed v in terms of R and omega.',
                    'Calculate the linear speed.',
                    'What is the period of one complete revolution?',
                    'Define centripetal acceleration.'
                ]
            },
            # Set 5
            {
                'question': 'A 3 kg block rests on a horizontal surface with coefficient of friction mu = 0.3.',
                'subquestions': [
                    'Calculate the normal force N.',
                    'What is the maximum static friction force?',
                    'Define the direction of friction force.',
                    'If F = 10 N is applied horizontally, will the block move? (Show calculation)'
                ]
            },
            # Set 6
            {
                'question': 'A simple pendulum has length L = 1 m and mass m = 0.5 kg. (g = 10 m/s^2)',
                'subquestions': [
                    'Write the formula for natural frequency omega_n = sqrt(g/L).',
                    'Calculate omega_n.',
                    'Find the period T.',
                    'Does the period depend on mass? Explain briefly.'
                ]
            },
            # Set 7
            {
                'question': 'For a double pendulum, both masses are 1 kg and both lengths are 1 m.',
                'subquestions': [
                    'How many degrees of freedom does this system have?',
                    'Name the generalized coordinates.',
                    'Write the expression for Lagrangian L = ?',
                    'Is this a conservative system? Why?'
                ]
            },
            # Set 8
            {
                'question': 'A wheel of radius R = 0.4 m rolls without slipping with center velocity v = 3 m/s.',
                'subquestions': [
                    'Write the no-slip condition relating v and angular velocity omega.',
                    'Calculate omega.',
                    'What is the velocity of the contact point?',
                    'Find the velocity of the topmost point.'
                ]
            },
            # Set 9
            {
                'question': 'Consider a rotating platform with angular velocity omega = 2 rad/s.',
                'subquestions': [
                    'Define Coriolis acceleration.',
                    'If a particle moves radially outward at 1 m/s, calculate Coriolis acceleration magnitude (2omega  x  v).',
                    'In which direction does Coriolis acceleration act?',
                    'Name one real-world example of Coriolis effect.'
                ]
            },
            # Set 10
            {
                'question': 'A particle has spherical coordinates (R=10 m, theta=30°, phi=60°).',
                'subquestions': [
                    'Define the polar angle theta in spherical system.',
                    'Calculate the z-coordinate: z = R cos(theta).',
                    'What is the projection on xy-plane: rho = R sin(theta)?',
                    'Write x in terms of R, theta, phi.'
                ]
            }
        ]
        
        return mixed_banks[set_num - 1]
    
    def generate_q2(self, set_num):
        """Q2 - Projectile Motion (Easy) - 6 subquestions of 0.5 marks each"""
        
        # Vary initial velocity, angle, and gravity
        projectile_params = [
            {'v0': 20, 'angle': 30, 'g': 10, 'h0': 0},
            {'v0': 15, 'angle': 45, 'g': 9.8, 'h0': 0},
            {'v0': 25, 'angle': 60, 'g': 10, 'h0': 0},
            {'v0': 18, 'angle': 30, 'g': 9.8, 'h0': 5},
            {'v0': 22, 'angle': 45, 'g': 10, 'h0': 0},
            {'v0': 16, 'angle': 53, 'g': 10, 'h0': 0},  # 53° gives nice values
            {'v0': 20, 'angle': 37, 'g': 10, 'h0': 0},  # 37° is 3-4-5 triangle
            {'v0': 24, 'angle': 45, 'g': 10, 'h0': 2},
            {'v0': 15, 'angle': 60, 'g': 9.8, 'h0': 0},
            {'v0': 25, 'angle': 30, 'g': 10, 'h0': 0},
        ]
        
        params = projectile_params[set_num - 1]
        v0 = params['v0']
        angle = params['angle']
        g = params['g']
        h0 = params['h0']
        
        angle_rad = math.radians(angle)
        v0x = v0 * math.cos(angle_rad)
        v0y = v0 * math.sin(angle_rad)
        
        height_str = f" from height h_0 = {h0} m" if h0 > 0 else ""
        
        return {
            'question': f'A projectile is launched{height_str} with initial velocity v_0 = {v0} m/s at angle theta = {angle}° to the horizontal. Take g = {g} m/s^2.',
            'subquestions': [
                f'Calculate the horizontal component of initial velocity (v_0_x = v_0 cos theta).',
                f'Calculate the vertical component of initial velocity (v_0_y = v_0 sin theta).',
                f'Write the position vector r_vec(t) = x(t)i + y(t)j as a function of time.',
                f'Find the time to reach maximum height (when v_y = 0).',
                f'Calculate the maximum height reached above the launch point.',
                f'Find the total time of flight (when y returns to ground level).'
            ]
        }
    
    def generate_q3(self, set_num):
        """Q3 - Coordinate Transformations (Half Medium, Half Extremely Difficult) - 6 subquestions"""
        
        coord_problems = [
            # Set 1: Cartesian to Polar (Medium then Hard)
            {
                'question': 'Consider coordinate transformations:',
                'subquestions': [
                    'A point has Cartesian coordinates (6, 8) meters. Find the polar radius r.',
                    'Calculate the polar angle theta in radians for the above point.',
                    'Now consider a point with polar coordinates (r=13 m, theta=67.38°). Find x and y.',
                    'A particle moves along r(t) = 5 + 2t meters, theta(t) = 0.5t radians. Find dr/dt and dtheta/dt.',
                    'Calculate the radial velocity component v_r = dr/dt at t = 2 seconds.',
                    'Find the transverse velocity component v_theta = r(dtheta/dt) at t = 2 seconds.'
                ]
            },
            # Set 2: Cylindrical coordinates (Medium then Hard)
            {
                'question': 'Work with cylindrical coordinates (rho, phi, z):',
                'subquestions': [
                    'Convert Cartesian point (3, 4, 5) meters to cylindrical coordinates. Find rho.',
                    'Find the angle phi for the above point.',
                    'What is the z-coordinate in cylindrical system?',
                    'A point moves with rho(t) = 2 m, phi(t) = pi*t rad, z(t) = 3t m. Find the position at t = 1 second in Cartesian.',
                    'Calculate the velocity in Cartesian coordinates at t = 1 second (x_vec_dot components).',
                    'Find the magnitude of velocity vector at t = 1 second.'
                ]
            },
            # Set 3: Spherical coordinates (Medium then Hard)
            {
                'question': 'Consider spherical coordinates (R, theta, phi) where theta is from z-axis:',
                'subquestions': [
                    'Convert (x=2, y=2, z=1) meters to spherical. Find R = sqrt(x^2+y^2+z^2).',
                    'Calculate theta = arccos(z/R).',
                    'Find phi = arctan(y/x).',
                    'A satellite has R = 7000 km, theta = 45°, phi = 30°. Find the z-coordinate.',
                    'Calculate the projection on xy-plane: rho = R sin theta.',
                    'Express the Cartesian velocity components for R(t) = 7000 km, theta(t) = 45°, phi(t) = 0.001t rad.'
                ]
            },
            # Set 4: Mixed transformation with motion
            {
                'question': 'Analyze motion in different coordinate systems:',
                'subquestions': [
                    'A point has (x=5, y=12) meters. Convert to polar (r, theta).',
                    'The point now moves to (x=7, y=24). Find new polar coordinates.',
                    'Calculate Deltar and Deltatheta between these two positions.',
                    'If motion is circular with r = 10 m constant, theta increasing at 0.5 rad/s, find v_theta.',
                    'For the same motion, write acceleration components a_r and a_theta (omega = 0.5 rad/s).',
                    'Verify that total acceleration magnitude for this circular motion is r omega^2.'
                ]
            },
            # Set 5: Polar velocity transformation
            {
                'question': 'Solve coordinate transformation problems:',
                'subquestions': [
                    'Point A: (x=-3, y=4) meters. Find polar coordinates r and theta (in degrees).',
                    'Point B: Polar (r=10 m, theta=120°). Convert to Cartesian.',
                    'The velocity in polar is v_r = 2 m/s, v_theta = 3 m/s at r = 5 m, theta = 30°. Find v_x.',
                    'Find v_y using v_x = v_r cos theta - v_theta sin theta, v_y = v_r sin theta + v_theta cos theta.',
                    'Calculate the total speed |v_vec|.',
                    'What angle does velocity make with the x-axis?'
                ]
            },
            # Set 6: Cylindrical helix motion
            {
                'question': 'A particle moves in a helical path:',
                'subquestions': [
                    'Cylindrical coords: rho = 2 m, phi(t) = t rad, z(t) = 0.5t m. Find position at t = 2π seconds.',
                    'How many complete revolutions has the particle made at t = 2π?',
                    'What is the vertical rise per revolution (pitch)?',
                    'Calculate drho/dt, dphi/dt, and dz/dt.',
                    'Find the cylindrical velocity components: v_rho, v_phi, v_z.',
                    'Convert velocity to Cartesian at t = π seconds and find magnitude.'
                ]
            },
            # Set 7: Spherical to Cartesian with velocity
            {
                'question': 'Analyze spherical coordinate motion:',
                'subquestions': [
                    'Satellite: R = 8000 km, theta = 30° (from z-axis), phi = 45°. Find x-coordinate.',
                    'Find y-coordinate.',
                    'Find z-coordinate.',
                    'Satellite rotates: R constant, theta constant, phi(t) = omegat with omega = 0.001 rad/s. Derive v_x.',
                    'Find v_y for the above motion.',
                    'Calculate orbital speed |v_vec| = R sin(theta)  x  omega.'
                ]
            },
            # Set 8: Time-varying transformation
            {
                'question': 'Advanced coordinate transformation with time-dependence:',
                'subquestions': [
                    'Motion: r(t) = 3 + 0.5t meters, theta(t) = 0.2t^2 radians. Find r and theta at t = 2 s.',
                    'Calculate velocity components: v_r = dr/dt and v_theta = r  x  dtheta/dt at t = 2 s.',
                    'Find acceleration components: a_r = d^2r/dt^2 - r(dtheta/dt)^2 at t = 2 s.',
                    'Calculate a_theta = r  x  d^2theta/dt^2 + 2(dr/dt)(dtheta/dt) at t = 2 s.',
                    'Convert (r, theta) at t = 2 s to Cartesian (x, y).',
                    'Verify acceleration magnitude: |a_vec| = sqrt(a_r^2 + a_theta^2).'
                ]
            },
            # Set 9: Combined cylindrical-spherical
            {
                'question': 'Multi-system coordinate analysis:',
                'subquestions': [
                    'Point P: Cylindrical (rho=5 m, phi=37°, z=12 m). Convert to Cartesian.',
                    'Convert the same point to spherical coordinates (R, theta, phi).',
                    'Verify R^2 = rho^2 + z^2.',
                    'Motion in cylindrical: rho(t) = 3t, phi(t) = 0.5t, z(t) = 4t. Find velocity v_vec at t = 1 s in Cartesian.',
                    'Calculate the speed at t = 1 second.',
                    'Find the angle the velocity makes with the z-axis (use v_z component).'
                ]
            },
            # Set 10: Complex 3D motion
            {
                'question': 'Solve advanced 3D coordinate transformations:',
                'subquestions': [
                    'Spherical: R = 15 m, theta = 60°, phi = 30°. Transform to Cartesian.',
                    'Transform to cylindrical coordinates (rho, phi, z).',
                    'A particle spirals: R(t) = 10 + t, theta(t) = 45° (constant), phi(t) = 2t rad. Find position at t = 1 s.',
                    'Derive velocity using chain rule: dx/dt from x = R sin theta cos phi.',
                    'Calculate dy/dt from y = R sin theta sin phi.',
                    'Find speed |v_vec| = sqrt(v_x^2 + v_y^2 + v_z^2) at t = 1 second.'
                ]
            }
        ]
        
        return coord_problems[set_num - 1]
    
    def generate_q4(self, set_num):
        """Q4 - Advanced/Difficult Numerical from Syllabus - 6 subquestions"""
        
        advanced_problems = [
            # Set 1: Inclined plane with friction
            {
                'question': 'A block of mass m = 5 kg rests on an inclined plane at angle theta = 30° with coefficient of kinetic friction mu_k = 0.2. Take g = 10 m/s^2.',
                'subquestions': [
                    'Draw free body diagram. Identify all forces (Weight, Normal, Friction).',
                    'Resolve weight into components: W_parallel = mg sin theta and W_perp = mg cos theta.',
                    'Calculate the normal force N.',
                    'Find friction force f = mu_k N.',
                    'Apply Newton\'s 2nd law along the incline: ma = mg sin theta - f. Find acceleration a.',
                    'If released from rest, find the distance traveled in t = 3 seconds.'
                ]
            },
            # Set 2: Atwood machine
            {
                'question': 'Two masses m_1 = 4 kg and m_2 = 6 kg are connected by a massless string over a frictionless pulley. Take g = 10 m/s^2.',
                'subquestions': [
                    'For m_1: Write equation of motion (T - m_1g = m_1a_1).',
                    'For m_2: Write equation of motion (m_2g - T = m_2a_2).',
                    'State the constraint: a_1 = -a_2 (magnitudes equal, opposite directions).',
                    'Add equations to eliminate T. Derive a = g(m_2 - m_1)/(m_1 + m_2).',
                    'Calculate the acceleration magnitude.',
                    'Find the tension T in the string.'
                ]
            },
            # Set 3: Simple pendulum - Lagrangian
            {
                'question': 'A simple pendulum: length L = 2 m, mass m = 1 kg, small angle approximation. Take g = 10 m/s^2.',
                'subquestions': [
                    'Choose generalized coordinate theta (angle from vertical). How many DOF?',
                    'Write kinetic energy T = (1/2)m(L*theta_dot)^2.',
                    'Write potential energy V = -mgL cos theta. For small theta, approximate cos theta ~ 1 - theta^2/2.',
                    'Form Lagrangian L = T - V.',
                    'Apply Euler-Lagrange: d/dt(dL/d(theta_dot)) - dL/dtheta = 0. Derive theta_ddot + (g/L)theta = 0.',
                    'Find natural frequency omega_n = sqrt(g/L) and period T = 2*pi/omega_n.'
                ]
            },
            # Set 4: Mass-spring-damper
            {
                'question': 'Mass-spring system with damping: m = 2 kg, k = 32 N/m, damping c = 4 N*s/m.',
                'subquestions': [
                    'Write equation of motion: m(d^2x/dt^2) + c(dx/dt) + kx = 0.',
                    'Divide by m to get standard form: (d^2x/dt^2) + 2*zeta*omega_n*(dx/dt) + omega_n^2*x = 0.',
                    'Find natural frequency omega_n = sqrt(k/m).',
                    'Calculate damping ratio zeta = c/(2*sqrt(km)).',
                    'Determine if system is underdamped (zeta < 1), critically damped (zeta = 1), or overdamped (zeta > 1).',
                    'For underdamped, find damped frequency omega_d = omega_n*sqrt(1 - zeta^2).'
                ]
            },
            # Set 5: Rolling wheel with acceleration
            {
                'question': 'A wheel of radius R = 0.5 m rolls without slipping. Center has velocity v_c = 4 m/s and acceleration a_c = 2 m/s^2.',
                'subquestions': [
                    'Find angular velocity omega from no-slip condition v_c = Romega.',
                    'Find angular acceleration alpha from a_c = Ralpha.',
                    'Calculate velocity of top point: v_top = v_c + Romega.',
                    'Find velocity of bottom (contact) point using v_bottom = v_c - Romega.',
                    'For top point, find centripetal acceleration a_centripetal = omega^2R.',
                    'Calculate total acceleration of top point: a_top = a_c + Ralpha (tangential) + a_centripetal (normal).'
                ]
            },
            # Set 6: Double pendulum Lagrangian (simplified)
            {
                'question': 'Double pendulum: L_1 = L_2 = 1 m, m_1 = m_2 = 1 kg, small angles, g = 10 m/s^2.',
                'subquestions': [
                    'Identify generalized coordinates: theta_1, theta_2. How many DOF?',
                    'For small angles, write kinetic energy T ~ (1/2)m_1*L_1^2*(theta_1_dot)^2 + (1/2)m_2[L_1^2*(theta_1_dot)^2 + L_2^2*(theta_2_dot)^2].',
                    'Write potential energy V ~ -m_1*g*L_1*cos(theta_1) - m_2*g*(L_1*cos(theta_1) + L_2*cos(theta_2)).',
                    'Form Lagrangian L = T - V.',
                    'State Euler-Lagrange equations for theta_1 and theta_2 (no need to fully derive).',
                    'For equal lengths and masses, estimate natural frequency of first mode omega_1 ~ sqrt(g/L).'
                ]
            },
            # Set 7: Rotating platform with Coriolis
            {
                'question': 'A platform rotates at constant omega = 2 rad/s. A particle moves radially outward at v_rel = 3 m/s at position r = 4 m from center.',
                'subquestions': [
                    'Calculate centripetal acceleration a_cent = omega^2r.',
                    'Calculate Coriolis acceleration magnitude a_Cor = 2omega v_rel.',
                    'State the direction of Coriolis acceleration (perpendicular to v_rel, in rotating frame).',
                    'Find tangential velocity due to platform rotation: v_tang = omegar.',
                    'In the inertial frame, write total velocity components (radial and tangential).',
                    'Calculate total acceleration magnitude in rotating frame (including both centripetal and Coriolis).'
                ]
            },
            # Set 8: Projectile on incline
            {
                'question': 'A ball is thrown up an incline (angle alpha = 30°) with v_0 = 10 m/s at angle beta = 45° to the incline. g = 10 m/s^2.',
                'subquestions': [
                    'Define coordinate system: x along incline, y perpendicular to incline.',
                    'Resolve gravity: g_x = g sin alpha (down the incline), g_y = g cos alpha (perpendicular).',
                    'Find initial velocity components: v_0_x = v_0 cos beta, v_0_y = v_0 sin beta.',
                    'Write position equations: x(t) = v_0_x t - ½g_x t^2, y(t) = v_0_y t - ½g_y t^2.',
                    'Find time when ball lands on incline (y = 0).',
                    'Calculate range along incline at landing time.'
                ]
            },
            # Set 9: Constrained motion - bead on rotating wire
            {
                'question': 'A bead slides on a wire rotating at omega = 3 rad/s. Bead is at r = 0.5 m from pivot, sliding outward at (dr/dt) = 0.2 m/s.',
                'subquestions': [
                    'In polar coordinates, write velocity: v_vec = (dr/dt)*e_r + r*(dtheta/dt)*e_theta with (dtheta/dt) = omega.',
                    'Calculate radial velocity component v_r = (dr/dt).',
                    'Calculate tangential velocity component v_theta = r*omega.',
                    'Find speed |v_vec| = sqrt(v_r^2 + v_theta^2).',
                    'Calculate centripetal acceleration a_cent = r*omega^2.',
                    'Include Coriolis term: total radial acceleration a_r = r_ddot - r*omega^2. If r_ddot = 0, find a_r.'
                ]
            },
            # Set 10: Energy method for pendulum
            {
                'question': 'A pendulum: L = 1.5 m, m = 2 kg, released from theta_0 = 60°. g = 10 m/s^2.',
                'subquestions': [
                    'At release (theta = 60 deg), calculate potential energy V = m*g*L*(1 - cos(theta_0)).',
                    'At lowest point (theta = 0), potential energy V = 0. State energy conservation.',
                    'Find kinetic energy at lowest point: T = (1/2)*m*(L*theta_dot)^2.',
                    'Using energy conservation, solve for angular velocity theta_dot at lowest point.',
                    'Calculate linear speed v = L*theta_dot at lowest point.',
                    'Find tension in string at lowest point: T = m*g + m*v^2/L.'
                ]
            }
        ]
        
        return advanced_problems[set_num - 1]


def main():
    """Main function to generate all question papers"""
    print("=" * 60)
    print("DYNAMIC SYSTEMS MODELING - QUESTION PAPER GENERATOR")
    print("=" * 60)
    print(f"\nGenerating 10 question paper sets...")
    print(f"Exam Date: 19-02-2026")
    print(f"Duration: 45 minutes")
    print(f"Total Marks: 10")
    print("\nPattern:")
    print("  - Q1 (Compulsory): 4 marks")
    print("  - Solve ANY TWO from Q2/Q3/Q4: 6 marks")
    print("\n" + "=" * 60)
    
    generator = QuestionPaperGenerator()
    generator.generate_all_sets(10)
    
    if not REPORTLAB_AVAILABLE:
        print("\n" + "=" * 60)
        print("📌 NOTE: HTML files generated successfully!")
        print("   To convert to PDF, you can:")
        print("   1. Open HTML files in a browser and Print to PDF")
        print("   2. Or install ReportLab: pip install reportlab")
        print("=" * 60)


if __name__ == "__main__":
    main()
