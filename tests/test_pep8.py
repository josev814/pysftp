'''test pysftp module, setup.py and tests - uses py.test'''
from pep8 import StyleGuide


def test_pep8():
    '''pep8 check the source'''
    # list the specific files or directories to check, directories are recursed
    paths = ['pysftp', 'setup.py', 'tests']
    p8c = StyleGuide(quiet=True)
    report = p8c.check_files(paths=paths)
    report.print_statistics()
    assert report.get_count() == 0
