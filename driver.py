# dedutivo
# Backward

import contextlib
import sys

from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)

    
def hardware_diagnosis_questions():

    # engine.reset()      # Allows us to run tests multiple times.

    engine.activate('rules') #STUDENTS: you will need to edit the name of your rule file here

    print("doing proof")
    
    try:
        with engine.prove_goal('rules.what_to_do($action)') as gen: #STUDENTS: you will need to edit this line
            for vars, plan in gen:
                print("Seu diagnostico: %s" % (vars['action'])) #STUDENTS: you will need to edit this line
                break

    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("done")


