def get_home_content():
    return {
        'hero_title': 'CyberGuard',
        'hero_subtitle': 'Your trusted partner in digital security',
        'stats': [
            {'number': '50M+', 'label': 'Users Protected'},
            {'number': '24/7', 'label': 'Monitoring'},
            {'number': '99.9%', 'label': 'Uptime'},
            {'number': '150+', 'label': 'Countries'}
        ],
        'quotes': [
            {
                'text': 'Security is not a product, but a process.',
                'author': 'Bruce Schneier'
            },
            {
                'text': 'The only system which is truly secure is one which is switched off.',
                'author': 'Gene Spafford'
            },
            {
                'text': 'Privacy is not something that I\'m merely entitled to, it\'s an absolute prerequisite.',
                'author': 'Marlon Brando'
            }
        ],
        'features': [
            {
                'title': 'Incident Reporting',
                'description': 'Report cybercrime incidents quickly and securely.',
                'icon': 'shield'
            },
            {
                'title': 'Real-time News',
                'description': 'Stay updated with latest cybersecurity threats.',
                'icon': 'trending-up'
            },
            {
                'title': 'AI Assistant',
                'description': 'Get instant help from our intelligent chatbot.',
                'icon': 'message-circle'
            },
            {
                'title': 'Expert Resources',
                'description': 'Access professional cybersecurity guidance.',
                'icon': 'book-open'
            }
        ]
    }

def get_news_content():
    return [
        {
            'title': 'New Ransomware Variant Targets Healthcare Systems',
            'category': 'Malware',
            'date': 'Today',
            'severity': 'high'
        },
        {
            'title': 'Global Phishing Campaign Uses AI-Generated Emails',
            'category': 'Phishing', 
            'date': '2 hours ago',
            'severity': 'medium'
        },
        {
            'title': 'Zero-Day Vulnerability Found in Popular VPN Software',
            'category': 'Vulnerability',
            'date': '5 hours ago', 
            'severity': 'critical'
        },
        {
            'title': 'Cybersecurity Awareness Month: Best Practices Guide',
            'category': 'Education',
            'date': '1 day ago',
            'severity': 'info'
        },
        {
            'title': 'Nation-State Actors Target Critical Infrastructure',
            'category': 'APT',
            'date': '2 days ago',
            'severity': 'high'
        },
        {
            'title': 'New Multi-Factor Authentication Guidelines Released',
            'category': 'Guidelines',
            'date': '3 days ago',
            'severity': 'info'
        },
        {
            'title': 'Supply Chain Attack Affects Major Software Vendor',
            'category': 'Supply Chain',
            'date': '1 week ago',
            'severity': 'high'
        },
        {
            'title': 'Cryptocurrency Exchange Security Breach Analysis',
            'category': 'Breach',
            'date': '1 week ago',
            'severity': 'medium'
        }
    ]

def get_resources_content():
    return {
        'helplines': [
            {
                'country': 'United States',
                'agency': 'FBI Internet Crime Complaint Center',
                'phone': '1-855-292-3937',
                'website': 'www.ic3.gov',
                'available': '24/7'
            },
            {
                'country': 'United Kingdom', 
                'agency': 'Action Fraud',
                'phone': '0300 123 2040',
                'website': 'www.actionfraud.police.uk',
                'available': '24/7'
            },
            {
                'country': 'India',
                'agency': 'Cyber Crime Helpline',
                'phone': '155260',
                'website': 'cybercrime.gov.in',
                'available': '24/7'
            },
            {
                'country': 'Australia',
                'agency': 'ACSC ReportCyber',
                'phone': '1300 292 371',
                'website': 'www.cyber.gov.au',
                'available': '24/7'
            }
        ],
        'guides': [
            {
                'title': 'Recognizing Phishing Emails',
                'description': 'Learn to identify suspicious emails and protect your information.'
            },
            {
                'title': 'Password Security Best Practices',
                'description': 'Create strong passwords and use two-factor authentication.'
            },
            {
                'title': 'Safe Online Shopping',
                'description': 'Shop securely and protect your financial information.'
            },
            {
                'title': 'Social Media Privacy',
                'description': 'Configure privacy settings and share safely.'
            }
        ]
    }