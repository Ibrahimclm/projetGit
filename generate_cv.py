#!/usr/bin/env python3
"""
Professional CV Generator for Ibrahim Sy
Generates a clean, professional PDF CV suitable for cybersecurity consulting firms.
"""

from weasyprint import HTML, CSS
import os


def get_cv_html():
    """Return the HTML content for the CV"""
    return """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CV Ibrahim Sy - Consultant Cybersécurité</title>
</head>
<body>
    <div class="container">
        <!-- Header Section -->
        <header>
            <h1>IBRAHIM SY</h1>
            <p class="title">Consultant en Gouvernance, Risques, Conformité et Protection des Données</p>
            <div class="contact">
                <p>Clamart (92) – Île-de-France</p>
                <p>06 68 28 34 79 | ibrahim_sy@outlook.fr</p>
                <p>https://fr.linkedin.com/in/ibrahim-sy</p>
            </div>
        </header>

        <!-- Profile Section -->
        <section>
            <h2>PROFIL</h2>
            <p>Consultant en cybersécurité orienté gouvernance, gestion des risques et protection des données. Expérience dans la contribution à la structuration et à l'amélioration d'un dispositif de sécurité aligné sur ISO 27001 et sur les exigences du RGPD. Dispose d'un socle technique en administration systèmes et réseaux facilitant l'analyse des risques et le dialogue entre équipes techniques, métiers et direction.</p>
        </section>

        <!-- Professional Experience Section -->
        <section>
            <h2>EXPÉRIENCE PROFESSIONNELLE</h2>
            
            <div class="experience">
                <div class="experience-header">
                    <h3>Consultant Cybersécurité – Montée en expertise GRC &amp; Data Privacy</h3>
                    <span class="period">2023 – 2025</span>
                </div>
                <p class="experience-intro">Période consacrée au renforcement des compétences en gouvernance, gestion des risques et protection des données.</p>
                <ul>
                    <li>Certification ISO 27001 Lead Implementer</li>
                    <li>Approfondissement de la méthodologie EBIOS Risk Manager</li>
                    <li>Réalisation d'analyses de risques structurées</li>
                    <li>Élaboration de livrables : politique SSI, plan de traitement des risques, procédure de gestion des incidents</li>
                    <li>Travaux académiques sur la conformité RGPD</li>
                    <li>Veille réglementaire ISO 27001 et RGPD</li>
                </ul>
                <p class="note">Cette période a également inclus une phase de rétablissement physique, aujourd'hui finalisée, menée en parallèle de la montée en compétences professionnelles.</p>
            </div>

            <div class="experience">
                <div class="experience-header">
                    <h3>Ingénieur Cybersécurité Systèmes &amp; Réseaux</h3>
                    <span class="period">Septembre 2021 – Novembre 2023</span>
                </div>
                <p class="company">Vistory – Vélizy</p>
                <p class="experience-intro">Contexte : PME industrielle engagée dans une démarche ISO 27001</p>
                
                <h4>Gouvernance &amp; Organisation SSI</h4>
                <ul>
                    <li>Contribution à la mise en place d'un SMSI</li>
                    <li>Rédaction de Politique SSI et procédures</li>
                    <li>Procédure de gestion des incidents</li>
                    <li>Revues d'habilitations</li>
                    <li>Sensibilisation sécurité et RGPD</li>
                    <li>Reporting interne</li>
                </ul>

                <h4>Gestion des Risques</h4>
                <ul>
                    <li>Participation à la cartographie des risques</li>
                    <li>Plan de traitement des risques</li>
                    <li>Identification des actifs critiques</li>
                    <li>Démarche inspirée d'EBIOS Risk Manager</li>
                </ul>

                <h4>Coordination &amp; Expertise Technique</h4>
                <ul>
                    <li>Administration Windows et Linux</li>
                    <li>Active Directory</li>
                    <li>Architecture réseau sécurisée</li>
                    <li>Analyse d'incidents</li>
                    <li>Durcissement des systèmes</li>
                </ul>
            </div>
        </section>

        <!-- Skills Section -->
        <section>
            <h2>COMPÉTENCES</h2>
            <div class="skills-grid">
                <div class="skill-category">
                    <h4>Gouvernance &amp; Conformité</h4>
                    <ul>
                        <li>SMSI ISO 27001</li>
                        <li>Politique SSI</li>
                        <li>Plan de traitement des risques</li>
                        <li>Procédure de gestion des incidents</li>
                        <li>Sensibilisation RGPD</li>
                    </ul>
                </div>

                <div class="skill-category">
                    <h4>Gestion des Risques</h4>
                    <ul>
                        <li>Cartographie des risques</li>
                        <li>Identification des actifs</li>
                        <li>Priorisation des risques</li>
                        <li>Approche EBIOS RM</li>
                    </ul>
                </div>

                <div class="skill-category">
                    <h4>Protection des Données</h4>
                    <ul>
                        <li>Cadre RGPD</li>
                        <li>Intégration des exigences data protection</li>
                    </ul>
                </div>

                <div class="skill-category">
                    <h4>Administration &amp; Environnement Technique</h4>
                    <ul>
                        <li>Windows Server</li>
                        <li>Linux</li>
                        <li>Active Directory</li>
                        <li>VLAN / VPN</li>
                        <li>Nagios / Splunk</li>
                        <li>Jira / ServiceNow</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- Academic Projects Section -->
        <section>
            <h2>PROJETS ACADÉMIQUES SIGNIFICATIFS</h2>
            <div class="project">
                <h4>Analyse de risques – EBIOS Risk Manager</h4>
                <p>Actifs essentiels, scénarios de menace, plan de traitement</p>
            </div>
            <div class="project">
                <h4>Étude de conformité RGPD</h4>
                <p>Analyse obligations, cartographie traitements, mesures organisationnelles</p>
            </div>
        </section>

        <!-- Education Section -->
        <section>
            <h2>FORMATION</h2>
            <ul>
                <li><strong>Expert en Cybersécurité des Systèmes d'Information – EPITA (RNCP 7)</strong></li>
                <li><strong>Mastère 2 – Expert IT Cybersécurité</strong></li>
                <li><strong>Développeur Intégrateur Web</strong></li>
            </ul>
        </section>

        <!-- Certifications Section -->
        <section>
            <h2>CERTIFICATIONS</h2>
            <ul>
                <li>ISO 27001 Lead Implementer</li>
                <li>MOOC ANSSI – SecNumAcademy</li>
                <li>MOOC CNIL – RGPD</li>
                <li>MOOC EBIOS Risk Manager</li>
                <li>Certification Manager de projets informatiques</li>
            </ul>
        </section>

        <!-- Languages Section -->
        <section>
            <h2>LANGUES</h2>
            <ul class="languages">
                <li><strong>Français :</strong> langue maternelle</li>
                <li><strong>Anglais :</strong> niveau B1</li>
                <li><strong>Arabe :</strong> niveau B1</li>
            </ul>
        </section>

        <!-- Additional Information Section -->
        <section>
            <h2>INFORMATIONS COMPLÉMENTAIRES</h2>
            <p>Reconnaissance de la Qualité de Travailleur Handicapé (RQTH)</p>
        </section>
    </div>
</body>
</html>
"""


def get_cv_css():
    """Return the CSS styling for the CV"""
    return """
@page {
    size: A4;
    margin: 1.5cm 2cm;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Helvetica', 'Arial', sans-serif;
    font-size: 10pt;
    line-height: 1.5;
    color: #2c3e50;
}

.container {
    max-width: 100%;
}

/* Header Styles */
header {
    text-align: center;
    padding-bottom: 15px;
    border-bottom: 2px solid #1a3a52;
    margin-bottom: 20px;
}

header h1 {
    font-size: 24pt;
    font-weight: 700;
    color: #1a3a52;
    margin-bottom: 5px;
    letter-spacing: 1px;
}

header .title {
    font-size: 11pt;
    color: #34495e;
    font-weight: 500;
    margin-bottom: 8px;
}

header .contact {
    font-size: 9pt;
    color: #5a6c7d;
    line-height: 1.4;
}

header .contact p {
    margin: 2px 0;
}

/* Section Styles */
section {
    margin-bottom: 18px;
    page-break-inside: avoid;
}

section h2 {
    font-size: 13pt;
    font-weight: 700;
    color: #1a3a52;
    text-transform: uppercase;
    border-bottom: 1px solid #d0d8e0;
    padding-bottom: 4px;
    margin-bottom: 10px;
    letter-spacing: 0.5px;
}

section p {
    text-align: justify;
    margin-bottom: 8px;
}

/* Experience Styles */
.experience {
    margin-bottom: 15px;
    page-break-inside: avoid;
}

.experience-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 4px;
}

.experience-header h3 {
    font-size: 11pt;
    font-weight: 600;
    color: #2c3e50;
    flex: 1;
}

.experience-header .period {
    font-size: 9pt;
    color: #5a6c7d;
    font-weight: 500;
    white-space: nowrap;
    margin-left: 10px;
}

.company {
    font-size: 10pt;
    color: #5a6c7d;
    font-style: italic;
    margin-bottom: 4px;
}

.experience-intro {
    font-size: 9.5pt;
    color: #5a6c7d;
    margin-bottom: 6px;
}

.experience h4 {
    font-size: 10pt;
    font-weight: 600;
    color: #34495e;
    margin-top: 8px;
    margin-bottom: 4px;
}

.experience ul {
    margin-left: 18px;
    margin-bottom: 6px;
}

.experience ul li {
    font-size: 9.5pt;
    margin-bottom: 2px;
    line-height: 1.4;
}

.note {
    font-size: 9pt;
    color: #5a6c7d;
    font-style: italic;
    margin-top: 6px;
}

/* Skills Grid */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
}

.skill-category {
    page-break-inside: avoid;
}

.skill-category h4 {
    font-size: 10pt;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 4px;
}

.skill-category ul {
    margin-left: 18px;
}

.skill-category ul li {
    font-size: 9.5pt;
    margin-bottom: 2px;
    line-height: 1.3;
}

/* Projects */
.project {
    margin-bottom: 8px;
    page-break-inside: avoid;
}

.project h4 {
    font-size: 10pt;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 2px;
}

.project p {
    font-size: 9.5pt;
    color: #5a6c7d;
    margin-bottom: 0;
}

/* General Lists */
section > ul {
    margin-left: 18px;
}

section > ul li {
    font-size: 9.5pt;
    margin-bottom: 3px;
    line-height: 1.4;
}

section > ul li strong {
    color: #2c3e50;
}

.languages li {
    line-height: 1.5;
}

/* Print optimization */
@media print {
    body {
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }
}
"""


def generate_cv_pdf(output_path="CV_Ibrahim_Sy.pdf"):
    """
    Generate the CV PDF file
    
    Args:
        output_path: Path where the PDF will be saved
    """
    html_content = get_cv_html()
    css_content = get_cv_css()
    
    # Create HTML object and render to PDF
    html = HTML(string=html_content)
    css = CSS(string=css_content)
    
    html.write_pdf(output_path, stylesheets=[css])
    print(f"CV generated successfully: {output_path}")
    
    # Check file size
    if os.path.exists(output_path):
        size = os.path.getsize(output_path)
        print(f"File size: {size / 1024:.2f} KB")


if __name__ == "__main__":
    generate_cv_pdf()
