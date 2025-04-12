echo "# new_repository" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Fa11en-Ange1/new_repository.git
git push -u origin main
