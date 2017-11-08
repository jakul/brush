from pathlib import Path

from app.api import app

if __name__ == '__main__':
    # Restart server when the .env file changes
    files_to_watch = [str(Path(__file__).parent / '.env')]

    # Restart server when any YAML file changes
    files_to_watch.extend([
        str(path) for path in Path('.').glob('app/**/*.yaml')
    ])

    app.run(
        debug=app.config['DEBUG'],
        # host=app.config['HOST'],
        # port=int(app.config['PORT']),
        # threaded=app.config['DEBUG'],
        # extra_files=files_to_watch,
    )
