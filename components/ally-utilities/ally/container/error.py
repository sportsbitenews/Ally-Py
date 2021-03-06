'''
Created on Jan 8, 2013

@package: ally utilities
@copyright: 2011 Sourcefabric o.p.s.
@license: http://www.gnu.org/licenses/gpl-3.0.txt
@author: Gabriel Nistor

Defines the errors for the IoC module.
'''

# --------------------------------------------------------------------

class SetupError(Exception):
    '''
    Exception thrown when there is a setup problem.
    '''

class ConfigError(Exception):
    '''
    Exception thrown when there is a configuration problem.
    '''

class AOPError(Exception):
    '''
    Exception thrown when there is a AOP problem.
    '''

