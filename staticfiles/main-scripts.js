 function copyLink() {
            const linkInput = document.getElementById("generatedLink");
            // Select the text field
            linkInput.select();
            linkInput.setSelectionRange(0, 99999); 
            // Copy the text inside the text field
            try {
                document.execCommand("copy");
                alert("[STATUS: OK] PATH COPIED TO SYSTEM BUFFER.");
            } catch (err) {
                console.error('Failed to copy text: ', err);
                alert("[STATUS: ERROR] FAILED TO COPY PATH.");
            }
        }