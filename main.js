document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.qa-button').forEach(function(button) {
        button.addEventListener('click', function () {
            var answers = this.parentNode.querySelector('.qa-answer').textContent.trim().split(',');
            this.parentNode.querySelectorAll('[name="ipt_options"]').forEach(element => {
                element.parentNode.classList.remove('qa-options-collect');
                element.parentNode.classList.remove('qa-options-incollect');
                if (answers.includes(element.value)) {
                    element.parentNode.classList.add('qa-options-collect');
                }
                else if (element.checked) {
                    element.parentNode.classList.add('qa-options-incollect');
                }
            });
        });
    });
});