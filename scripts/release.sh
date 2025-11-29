#!/usr/bin/env bash
# Script to bump version, create tag, and trigger release
#
# Usage:
#   ./scripts/release.sh patch  # 0.1.0 -> 0.1.1
#   ./scripts/release.sh minor  # 0.1.0 -> 0.2.0
#   ./scripts/release.sh major  # 0.1.0 -> 1.0.0

set -e

if [ -z "$1" ]; then
    echo "Usage: $0 <major|minor|patch>"
    exit 1
fi

PART=$1

if [ "$(git branch --show-current)" != "main" ]; then
    echo "Error: Must be on main branch"
    exit 1
fi

echo "Fetching latest changes..."
git fetch origin

if [ "$(git rev-parse HEAD)" != "$(git rev-parse origin/main)" ]; then
    echo "Error: Local main is not up to date with origin/main"
    exit 1
fi

echo "Running tests..."
pytest

echo "Running linter..."
ruff check .

echo "Bumping $PART version..."
bump-my-version bump "$PART"

echo "Pushing changes and tags..."
git push origin main --tags

echo ""
echo "✅ Version bumped and tag pushed!"
echo "🚀 GitHub Actions will now:"
echo "   1. Create a GitHub release"
echo "   2. Build the package"
echo "   3. Publish to PyPI"
echo ""
echo "Monitor progress at:"
echo "https://github.com/konsulten/python-sn2/actions"
