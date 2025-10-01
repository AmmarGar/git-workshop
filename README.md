
# Git Workshop for Beginners: Git CLI and GitHub CLI

Welcome to this beginner-friendly workshop on Git and GitHub, focusing on command-line tools (Git CLI and GitHub CLI, or `gh`). We will cover cloning, forking, branching, pull requests (PRs), merge conflicts, and PR reviews. This workshop assumes no prior experience but requires a computer with terminal access.

The exercises use this repository, which includes:
- `names.py`: A simple Python script where you will add your name.
- This README: Step-by-step instructions.

**Prerequisites:**
- A GitHub account (create one at [github.com](https://github.com) if needed).
- Basic terminal familiarity (e.g., navigating directories with `cd`).

## Step 0: Install Git and GitHub CLI

Before starting, install Git (for version control) and GitHub CLI (`gh`, for GitHub interactions via terminal).

### Installing on Ubuntu (Linux)
1. Open a terminal.
2. Install Git:
   ```
   sudo apt update
   sudo apt install git
   ```
3. Install GitHub CLI:
   ```
   sudo mkdir -p -m 755 /etc/apt/keyrings
   curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/etc/apt/keyrings/githubcli-archive-keyring.gpg
   sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
   sudo apt update
   sudo apt install gh
   ```
4. Verify installations:
   ```
   git --version
   gh --version
   ```
5. Authenticate `gh` (run `gh auth login` and follow prompts).

### Installing on Windows
1. Install Git: Download and run the installer from [git-scm.com/download/win](https://git-scm.com/download/win). Use default settings.
2. Install GitHub CLI: If you have Winget (Windows Package Manager, included in Windows 10+), open Command Prompt or PowerShell and run:
   ```
   winget install --id GitHub.cli
   ```
   Alternatively, download the MSI installer from [cli.github.com](https://cli.github.com).
3. Verify installations (in Command Prompt or PowerShell):
   ```
   git --version
   gh --version
   ```
4. Authenticate `gh` (run `gh auth login` and follow prompts).

**Note:** If issues arise, refer to official docs: [Git Installation](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [GitHub CLI Installation](https://cli.github.com/manual/installation).

## Step 1: Clone the Repository
Cloning creates a local copy of the remote repository.

1. Navigate to your desired directory:
   ```
   cd path/to/your/folder
   ```
2. Clone this repo (replace `<repo-url>` with the actual URL, e.g., https://github.com/yourusername/git-workshop-beginners.git):
   ```
   git clone <repo-url>
   ```
3. Enter the repo directory:
   ```
   cd git-workshop-beginners
   ```

This uses pure Git CLI. Now you have a local copy.

## Step 2: Fork the Repository Using GitHub CLI
Forking creates your own copy on GitHub for independent changes. We use `gh` for speed.

1. Ensure you're in the repo directory.
2. Fork the repo:
   ```
   gh repo fork --remote
   ```
   - This forks to your GitHub account and adds a remote called `origin` pointing to your fork.
   - **Note on underlying Git commands:** `gh repo fork` essentially performs:
     - API call to GitHub to create the fork (no direct Git equivalent).
     - `git remote add origin <your-fork-url>` to link your local repo to the fork.

Now, your changes will go to your fork. The original repo is upstream (remote often named `upstream`—add it if needed: `git remote add upstream <original-repo-url>`).

## Step 3: Create a Branch and Add Your Name (Emphasizing Branches)
Branches allow parallel work without affecting the main codebase. **Always use branches for changes—never commit directly to `main`!** This prevents conflicts and enables reviews.

1. Create and switch to a new branch (replace `<your-name>` with your name, e.g., `add-alice`):
   ```
   git checkout -b add-<your-name>
   ```
   - This creates a branch from `main` and switches to it.

2. Edit `names.py` to add your name:
   - Open `names.py` in a text editor.
   - Change `names = []` to `names = ["YourName"]` (replace with your actual name).
   - Save the file.

3. Stage and commit the change:
   ```
   git add names.py
   git commit -m "Add my name to the list"
   ```

4. Push the branch to your fork:
   ```
   git push -u origin add-<your-name>
   ```

**Branching emphasis:** Always create a new branch before making any changes. Never work on the main or master branch!

## Step 4: Open a Pull Request Using GitHub CLI
PRs propose changes for review and merging.

1. Create a PR from your branch to the original repo's `main`:
   ```
   gh pr create"
   ```
   - **Note on underlying Git commands:** `gh pr create` handles:
     - Pushing the branch (if not done).
     - API call to create the PR (no direct Git CLI equivalent).

The instructor will merge their PR first, updating `main` and creating potential conflicts for others.

## Step 5: Handle Merge Conflicts via Rebase
After the instructor merges their PR, your branch may conflict with the updated `main`.

1. Fetch upstream changes:
   ```
   git fetch upstream
   ```

2. Rebase your branch on upstream `main`:
   ```
   git rebase upstream/main
   ```
   - If conflicts occur (e.g., both modified the `names` list), Git will pause.
   - Open the conflicting file (`names.py`), resolve manually (e.g., combine lists: `names = ["InstructorName", "YourName"]`).
   - Stage the resolved file: `git add names.py`.
   - Continue rebase: `git rebase --continue`.

3. Force-push the rebased branch:
   ```
   git push --force-with-lease origin add-<your-name>
   ```

This teaches conflict resolution. Rebasing rewrites history for a clean timeline.

## Step 6: Review a Pull Request
The instructor will create a new PR (e.g., adding a feature or bug to `names.py`).

1. Checkout the PR locally using GitHub CLI:
   ```
   gh pr checkout <pr-number>
   ```
   - This creates a local branch for the PR.
   - **Note on underlying Git commands:** `gh pr checkout` performs:
     - `git fetch` from the PR's remote.
     - `git checkout` to a new branch.

2. Test the changes:
   - Run `python names.py` to verify.
   - Check for issues (e.g., does it print correctly?).

3. Leave a review on GitHub web interface:
   - Go to the PR URL (from `gh pr view <pr-number>`).
   - Add comments, approve, or request changes via the web.

