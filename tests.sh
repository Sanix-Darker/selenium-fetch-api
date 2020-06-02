# Copy the config txt file to tests directory
cp ./config.txt ./tests/
pytest

# Then you delete it again
rm -rf ./tests/config.txt
