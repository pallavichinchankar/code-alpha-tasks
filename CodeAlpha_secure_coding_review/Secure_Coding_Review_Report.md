# Secure Coding Review Report
## CodeAlpha Cyber Security Internship – Task 3

---

## Application Reviewed
- Type: Web Application (Login System)
- Language: PHP
- Review Method: Manual Code Review
- Reference: OWASP Top 10

---

## Identified Vulnerabilities

### 1. SQL Injection
- User input is directly inserted into the SQL query without sanitization.
- This allows attackers to manipulate the query logic.
- Example payload:
' OR '1'='1

yaml
Copy code
- Impact: Authentication bypass and unauthorized access.

---

### 2. Plain Text Password Storage
- Passwords are stored and compared in plain text.
- No hashing or encryption is used.
- Impact: If the database is compromised, all user passwords are exposed.

---

### 3. No Input Validation
- User inputs are not validated or sanitized.
- Malicious payloads can be injected into the application.
- Impact: Leads to SQL Injection and other injection-based attacks.

---

### 4. Insecure Session Handling
- No session regeneration after login.
- The application is vulnerable to session fixation attacks.
- Impact: Attackers can hijack authenticated sessions.

---

## Remediation and Secure Coding Practices
- Use prepared statements to prevent SQL Injection.
- Store passwords securely using bcrypt hashing (`password_hash()`).
- Validate and sanitize all user inputs before processing.
- Implement secure session management and regenerate session IDs after login.
- Apply the principle of least privilege for database users.
- Enable proper error logging instead of displaying detailed errors to users.

---

## Conclusion
The application contained multiple critical security vulnerabilities.
After applying secure coding practices, the login system is protected
against common web attacks such as SQL Injection and credential theft.