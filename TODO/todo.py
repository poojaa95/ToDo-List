from flask import Flask, render_template, request

app = Flask(__name__)

todo = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Add tasks
        if "add_task" in request.form:
            tasks_input = request.form['tasks']
            tasks = [t.strip() for t in tasks_input.split(",") if t.strip()]
            todo.extend(tasks)

        # Update status (via button or checkbox)
        elif "update_status" in request.form:
            task_index = int(request.form['task_index'])
            status = request.form['status']

            if status == "completed":
                todo[task_index] = todo[task_index].split(" (marked as read.)")[0] + " (marked as read.)"
            elif status == "pending":
                todo[task_index] = todo[task_index].replace(" (marked as read.)", "")

        # Delete task
        elif "delete_task" in request.form:
            task_index = int(request.form['task_index'])
            todo.pop(task_index)

    return render_template("index.html", todo=todo)

if __name__ == "__main__":
    app.run(debug=True)
