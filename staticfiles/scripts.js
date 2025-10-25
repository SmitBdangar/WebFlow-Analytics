function togglePassword() {
            const passwordInput = document.getElementById('id_password');
            const toggleBtn = event.currentTarget;
            
            if (passwordInput.type === 'password') {
                passwordInput.type = 'text';
                toggleBtn.textContent = 'HIDE';
            } else {
                passwordInput.type = 'password';
                toggleBtn.textContent = 'SHOW';
            }
        }

        // Submit form on Enter key in password field
        document.getElementById('id_password').addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                document.querySelector('form').submit();
            }
        });

        // Add cursor blink effect to focused inputs
        const inputs = document.querySelectorAll('.terminal-input');
        inputs.forEach(input => {
            input.addEventListener('focus', function() {
                this.classList.add('cursor-blink');
            });
            input.addEventListener('blur', function() {
                this.classList.remove('cursor-blink');
            });
        });