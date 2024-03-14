# rules_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def what_to_do_check_power_requirement_vs_rating(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'power_comes_on', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.what_to_do_check_power_requirement_vs_rating: got unexpected plan from when clause 1"
            with engine.prove('questions', 'live_screen', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_do_check_power_requirement_vs_rating: got unexpected plan from when clause 2"
                with engine.prove('questions', 'new_build', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.what_to_do_check_power_requirement_vs_rating: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_do_connect_to_know_good_outlet(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'power_comes_on', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.what_to_do_connect_to_know_good_outlet: got unexpected plan from when clause 1"
            with engine.prove('questions', 'ac_power_source_tested', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_do_connect_to_know_good_outlet: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_do_select_proper_voltage_on_rear_of_power_suply(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'power_comes_on', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.what_to_do_select_proper_voltage_on_rear_of_power_suply: got unexpected plan from when clause 1"
            with engine.prove('questions', 'ac_power_source_tested', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_do_select_proper_voltage_on_rear_of_power_suply: got unexpected plan from when clause 2"
                with engine.prove('questions', 'psu_universal_input', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.what_to_do_select_proper_voltage_on_rear_of_power_suply: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_do_make_sure_fonte_panel_switch_to_motherboard_lead_is_connected_to_the_proper_point(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'power_comes_on', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.what_to_do_make_sure_fonte_panel_switch_to_motherboard_lead_is_connected_to_the_proper_point: got unexpected plan from when clause 1"
            with engine.prove('questions', 'ac_power_source_tested', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_do_make_sure_fonte_panel_switch_to_motherboard_lead_is_connected_to_the_proper_point: got unexpected plan from when clause 2"
                with engine.prove('questions', 'psu_universal_input', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.what_to_do_make_sure_fonte_panel_switch_to_motherboard_lead_is_connected_to_the_proper_point: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'checked_motherboard_lead', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.what_to_do_make_sure_fonte_panel_switch_to_motherboard_lead_is_connected_to_the_proper_point: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_do_replace_switch_or_substitute_front_panel_reset_switch_if_available(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'power_comes_on', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.what_to_do_replace_switch_or_substitute_front_panel_reset_switch_if_available: got unexpected plan from when clause 1"
            with engine.prove('questions', 'ac_power_source_tested', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_do_replace_switch_or_substitute_front_panel_reset_switch_if_available: got unexpected plan from when clause 2"
                with engine.prove('questions', 'psu_universal_input', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.what_to_do_replace_switch_or_substitute_front_panel_reset_switch_if_available: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'checked_motherboard_lead', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.what_to_do_replace_switch_or_substitute_front_panel_reset_switch_if_available: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'power_switch_fail', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.what_to_do_replace_switch_or_substitute_front_panel_reset_switch_if_available: got unexpected plan from when clause 5"
                            rule.rule_base.num_bc_rule_successes += 1
                            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_do_remake_motherboard_power_connections(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'power_comes_on', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.what_to_do_remake_motherboard_power_connections: got unexpected plan from when clause 1"
            with engine.prove('questions', 'ac_power_source_tested', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_do_remake_motherboard_power_connections: got unexpected plan from when clause 2"
                with engine.prove('questions', 'psu_universal_input', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.what_to_do_remake_motherboard_power_connections: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'checked_motherboard_lead', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.what_to_do_remake_motherboard_power_connections: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'power_switch_fail', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.what_to_do_remake_motherboard_power_connections: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'psu_connections_to_motherboard_correct', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.what_to_do_remake_motherboard_power_connections: got unexpected plan from when clause 6"
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_do_defective_power_supply_test_on_2nd_pc_before_discarding(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'power_comes_on', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.what_to_do_defective_power_supply_test_on_2nd_pc_before_discarding: got unexpected plan from when clause 1"
            with engine.prove('questions', 'ac_power_source_tested', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_do_defective_power_supply_test_on_2nd_pc_before_discarding: got unexpected plan from when clause 2"
                with engine.prove('questions', 'psu_universal_input', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.what_to_do_defective_power_supply_test_on_2nd_pc_before_discarding: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'checked_motherboard_lead', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.what_to_do_defective_power_supply_test_on_2nd_pc_before_discarding: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'power_switch_fail', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.what_to_do_defective_power_supply_test_on_2nd_pc_before_discarding: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'psu_connections_to_motherboard_correct', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.what_to_do_defective_power_supply_test_on_2nd_pc_before_discarding: got unexpected plan from when clause 6"
                                with engine.prove('questions', 'forced_hard_drive_spin_up', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "rules.what_to_do_defective_power_supply_test_on_2nd_pc_before_discarding: got unexpected plan from when clause 7"
                                    with engine.prove('questions', 'hard_drive_tested_good', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "rules.what_to_do_defective_power_supply_test_on_2nd_pc_before_discarding: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_do_try_drive_in_test_pc_or_substitute_known_good_drive_for_testing(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'power_comes_on', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.what_to_do_try_drive_in_test_pc_or_substitute_known_good_drive_for_testing: got unexpected plan from when clause 1"
            with engine.prove('questions', 'ac_power_source_tested', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_do_try_drive_in_test_pc_or_substitute_known_good_drive_for_testing: got unexpected plan from when clause 2"
                with engine.prove('questions', 'psu_universal_input', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.what_to_do_try_drive_in_test_pc_or_substitute_known_good_drive_for_testing: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'checked_motherboard_lead', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.what_to_do_try_drive_in_test_pc_or_substitute_known_good_drive_for_testing: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'power_switch_fail', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.what_to_do_try_drive_in_test_pc_or_substitute_known_good_drive_for_testing: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'psu_connections_to_motherboard_correct', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.what_to_do_try_drive_in_test_pc_or_substitute_known_good_drive_for_testing: got unexpected plan from when clause 6"
                                with engine.prove('questions', 'forced_hard_drive_spin_up', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "rules.what_to_do_try_drive_in_test_pc_or_substitute_known_good_drive_for_testing: got unexpected plan from when clause 7"
                                    with engine.prove('questions', 'hard_drive_tested_good', context,
                                                      (rule.pattern(2),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "rules.what_to_do_try_drive_in_test_pc_or_substitute_known_good_drive_for_testing: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_do_strip_system_down_to_video_adapter_only_See_box_A_on_conflict_resolution_chart(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'power_comes_on', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.what_to_do_strip_system_down_to_video_adapter_only_See_box_A_on_conflict_resolution_chart: got unexpected plan from when clause 1"
            with engine.prove('questions', 'ac_power_source_tested', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_do_strip_system_down_to_video_adapter_only_See_box_A_on_conflict_resolution_chart: got unexpected plan from when clause 2"
                with engine.prove('questions', 'psu_universal_input', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.what_to_do_strip_system_down_to_video_adapter_only_See_box_A_on_conflict_resolution_chart: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'checked_motherboard_lead', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.what_to_do_strip_system_down_to_video_adapter_only_See_box_A_on_conflict_resolution_chart: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'power_switch_fail', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.what_to_do_strip_system_down_to_video_adapter_only_See_box_A_on_conflict_resolution_chart: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'psu_connections_to_motherboard_correct', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.what_to_do_strip_system_down_to_video_adapter_only_See_box_A_on_conflict_resolution_chart: got unexpected plan from when clause 6"
                                with engine.prove('questions', 'forced_hard_drive_spin_up', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "rules.what_to_do_strip_system_down_to_video_adapter_only_See_box_A_on_conflict_resolution_chart: got unexpected plan from when clause 7"
                                    with engine.prove('questions', 'bad_adapter_on_bus', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "rules.what_to_do_strip_system_down_to_video_adapter_only_See_box_A_on_conflict_resolution_chart: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_do_test_or_replace_power_supply(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'power_comes_on', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.what_to_do_test_or_replace_power_supply: got unexpected plan from when clause 1"
            with engine.prove('questions', 'ac_power_source_tested', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_do_test_or_replace_power_supply: got unexpected plan from when clause 2"
                with engine.prove('questions', 'psu_universal_input', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.what_to_do_test_or_replace_power_supply: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'checked_motherboard_lead', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.what_to_do_test_or_replace_power_supply: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'power_switch_fail', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.what_to_do_test_or_replace_power_supply: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'psu_connections_to_motherboard_correct', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.what_to_do_test_or_replace_power_supply: got unexpected plan from when clause 6"
                                with engine.prove('questions', 'forced_hard_drive_spin_up', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "rules.what_to_do_test_or_replace_power_supply: got unexpected plan from when clause 7"
                                    with engine.prove('questions', 'bad_adapter_on_bus', context,
                                                      (rule.pattern(0),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "rules.what_to_do_test_or_replace_power_supply: got unexpected plan from when clause 8"
                                        with engine.prove('questions', 'powers_motherboard_on_bench', context,
                                                          (rule.pattern(0),)) \
                                          as gen_9:
                                          for x_9 in gen_9:
                                            assert x_9 is None, \
                                              "rules.what_to_do_test_or_replace_power_supply: got unexpected plan from when clause 9"
                                            rule.rule_base.num_bc_rule_successes += 1
                                            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_do_either_you_have_a_short_circuit_in_the_case_or_a_geometry(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'power_comes_on', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.what_to_do_either_you_have_a_short_circuit_in_the_case_or_a_geometry: got unexpected plan from when clause 1"
            with engine.prove('questions', 'ac_power_source_tested', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_do_either_you_have_a_short_circuit_in_the_case_or_a_geometry: got unexpected plan from when clause 2"
                with engine.prove('questions', 'psu_universal_input', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.what_to_do_either_you_have_a_short_circuit_in_the_case_or_a_geometry: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'checked_motherboard_lead', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.what_to_do_either_you_have_a_short_circuit_in_the_case_or_a_geometry: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'power_switch_fail', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.what_to_do_either_you_have_a_short_circuit_in_the_case_or_a_geometry: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'psu_connections_to_motherboard_correct', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.what_to_do_either_you_have_a_short_circuit_in_the_case_or_a_geometry: got unexpected plan from when clause 6"
                                with engine.prove('questions', 'forced_hard_drive_spin_up', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "rules.what_to_do_either_you_have_a_short_circuit_in_the_case_or_a_geometry: got unexpected plan from when clause 7"
                                    with engine.prove('questions', 'bad_adapter_on_bus', context,
                                                      (rule.pattern(0),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "rules.what_to_do_either_you_have_a_short_circuit_in_the_case_or_a_geometry: got unexpected plan from when clause 8"
                                        with engine.prove('questions', 'powers_motherboard_on_bench', context,
                                                          (rule.pattern(1),)) \
                                          as gen_9:
                                          for x_9 in gen_9:
                                            assert x_9 is None, \
                                              "rules.what_to_do_either_you_have_a_short_circuit_in_the_case_or_a_geometry: got unexpected plan from when clause 9"
                                            rule.rule_base.num_bc_rule_successes += 1
                                            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_do_premature_power_good_signal_try_different_power_supply(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'power_comes_on', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.what_to_do_premature_power_good_signal_try_different_power_supply: got unexpected plan from when clause 1"
            with engine.prove('questions', 'live_screen', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_do_premature_power_good_signal_try_different_power_supply: got unexpected plan from when clause 2"
                with engine.prove('questions', 'new_build', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.what_to_do_premature_power_good_signal_try_different_power_supply: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'needs_two_tries_to_boot', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.what_to_do_premature_power_good_signal_try_different_power_supply: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_do_remove_latest_addition_and_retry(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'power_comes_on', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.what_to_do_remove_latest_addition_and_retry: got unexpected plan from when clause 1"
            with engine.prove('questions', 'live_screen', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_do_remove_latest_addition_and_retry: got unexpected plan from when clause 2"
                with engine.prove('questions', 'new_build', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.what_to_do_remove_latest_addition_and_retry: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'needs_two_tries_to_boot', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.what_to_do_remove_latest_addition_and_retry: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'hear_more_than_1_beep', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.what_to_do_remove_latest_addition_and_retry: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'new_hardware_installed', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.what_to_do_remove_latest_addition_and_retry: got unexpected plan from when clause 6"
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_do_age_requires_cleaning_obstruction_non_pwm_fan(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'power_comes_on', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.what_to_do_age_requires_cleaning_obstruction_non_pwm_fan: got unexpected plan from when clause 1"
            with engine.prove('questions', 'live_screen', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_do_age_requires_cleaning_obstruction_non_pwm_fan: got unexpected plan from when clause 2"
                with engine.prove('questions', 'new_build', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.what_to_do_age_requires_cleaning_obstruction_non_pwm_fan: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'needs_two_tries_to_boot', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.what_to_do_age_requires_cleaning_obstruction_non_pwm_fan: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'hear_more_than_1_beep', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.what_to_do_age_requires_cleaning_obstruction_non_pwm_fan: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'new_hardware_installed', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.what_to_do_age_requires_cleaning_obstruction_non_pwm_fan: got unexpected plan from when clause 6"
                                with engine.prove('questions', 'loud_fan_noise', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "rules.what_to_do_age_requires_cleaning_obstruction_non_pwm_fan: got unexpected plan from when clause 7"
                                    rule.rule_base.num_bc_rule_successes += 1
                                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_do_quality_stability_test_power_supply_or_not_a_psu_failure(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'power_comes_on', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.what_to_do_quality_stability_test_power_supply_or_not_a_psu_failure: got unexpected plan from when clause 1"
            with engine.prove('questions', 'live_screen', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.what_to_do_quality_stability_test_power_supply_or_not_a_psu_failure: got unexpected plan from when clause 2"
                with engine.prove('questions', 'new_build', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.what_to_do_quality_stability_test_power_supply_or_not_a_psu_failure: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'needs_two_tries_to_boot', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.what_to_do_quality_stability_test_power_supply_or_not_a_psu_failure: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'hear_more_than_1_beep', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.what_to_do_quality_stability_test_power_supply_or_not_a_psu_failure: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'new_hardware_installed', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.what_to_do_quality_stability_test_power_supply_or_not_a_psu_failure: got unexpected plan from when clause 6"
                                with engine.prove('questions', 'loud_fan_noise', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "rules.what_to_do_quality_stability_test_power_supply_or_not_a_psu_failure: got unexpected plan from when clause 7"
                                    with engine.prove('questions', 'hdd_or_os_error', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "rules.what_to_do_quality_stability_test_power_supply_or_not_a_psu_failure: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('rules')
  
  bc_rule.bc_rule('what_to_do_check_power_requirement_vs_rating', This_rule_base, 'what_to_do',
                  what_to_do_check_power_requirement_vs_rating, None,
                  (pattern.pattern_literal("Cheque a energia necessaria com a energia recebida"),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_do_connect_to_know_good_outlet', This_rule_base, 'what_to_do',
                  what_to_do_connect_to_know_good_outlet, None,
                  (pattern.pattern_literal("Conecte com uma fonte de energia confiável/já testada"),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_do_select_proper_voltage_on_rear_of_power_suply', This_rule_base, 'what_to_do',
                  what_to_do_select_proper_voltage_on_rear_of_power_suply, None,
                  (pattern.pattern_literal("Seleciona a voltagem correta na parte traseira da fonte"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_do_make_sure_fonte_panel_switch_to_motherboard_lead_is_connected_to_the_proper_point', This_rule_base, 'what_to_do',
                  what_to_do_make_sure_fonte_panel_switch_to_motherboard_lead_is_connected_to_the_proper_point, None,
                  (pattern.pattern_literal("Verifique se o painel da fonte esteja conectado corretamente com o cabo na placa-mae"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_do_replace_switch_or_substitute_front_panel_reset_switch_if_available', This_rule_base, 'what_to_do',
                  what_to_do_replace_switch_or_substitute_front_panel_reset_switch_if_available, None,
                  (pattern.pattern_literal("Substitua o switch ou substitua o switch de reset no painel frontal se disponivel"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_do_remake_motherboard_power_connections', This_rule_base, 'what_to_do',
                  what_to_do_remake_motherboard_power_connections, None,
                  (pattern.pattern_literal("Refaça a conexao dos cabos da fonte com a placa-mae"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_do_defective_power_supply_test_on_2nd_pc_before_discarding', This_rule_base, 'what_to_do',
                  what_to_do_defective_power_supply_test_on_2nd_pc_before_discarding, None,
                  (pattern.pattern_literal("Fonte de alimentação com defeito, teste a fonte em um pc secundário"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_do_try_drive_in_test_pc_or_substitute_known_good_drive_for_testing', This_rule_base, 'what_to_do',
                  what_to_do_try_drive_in_test_pc_or_substitute_known_good_drive_for_testing, None,
                  (pattern.pattern_literal("Teste o HD em outro pc ou use um HD bom para teste"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),
                   pattern.pattern_literal('false'),))
  
  bc_rule.bc_rule('what_to_do_strip_system_down_to_video_adapter_only_See_box_A_on_conflict_resolution_chart', This_rule_base, 'what_to_do',
                  what_to_do_strip_system_down_to_video_adapter_only_See_box_A_on_conflict_resolution_chart, None,
                  (pattern.pattern_literal("strip_system_down_to_video_adapter_only_See_box_A_on_conflict_resolution_chart"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_do_test_or_replace_power_supply', This_rule_base, 'what_to_do',
                  what_to_do_test_or_replace_power_supply, None,
                  (pattern.pattern_literal("Teste ou troque a fonte de alimentação"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_do_either_you_have_a_short_circuit_in_the_case_or_a_geometry', This_rule_base, 'what_to_do',
                  what_to_do_either_you_have_a_short_circuit_in_the_case_or_a_geometry, None,
                  (pattern.pattern_literal("Ou há um curto circuito no gabinete ou um problema geometrico colocando um estresse inaceitavel na placa-mae. Também é possível que o adaptador de vídeo não foi colocada corretamente, devido a posicao do suporte"),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_do_premature_power_good_signal_try_different_power_supply', This_rule_base, 'what_to_do',
                  what_to_do_premature_power_good_signal_try_different_power_supply, None,
                  (pattern.pattern_literal("Sinal de energia suficiente prematuramente, teste com outra fonte de alimentacao"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_do_remove_latest_addition_and_retry', This_rule_base, 'what_to_do',
                  what_to_do_remove_latest_addition_and_retry, None,
                  (pattern.pattern_literal("Remova o ultimo hardware instalado e tente novamente."),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_do_age_requires_cleaning_obstruction_non_pwm_fan', This_rule_base, 'what_to_do',
                  what_to_do_age_requires_cleaning_obstruction_non_pwm_fan, None,
                  (pattern.pattern_literal("Ou o fan pode estar velho, necessitando limpeza, obstruido ou o fan pode nao ser PWM"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_do_quality_stability_test_power_supply_or_not_a_psu_failure', This_rule_base, 'what_to_do',
                  what_to_do_quality_stability_test_power_supply_or_not_a_psu_failure, None,
                  (pattern.pattern_literal("ok"),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))


Krb_filename = '..\\rules.krb'
Krb_lineno_map = (
    ((14, 18), (2, 2)),
    ((20, 25), (4, 4)),
    ((26, 31), (5, 5)),
    ((32, 37), (6, 6)),
    ((50, 54), (9, 9)),
    ((56, 61), (11, 11)),
    ((62, 67), (12, 12)),
    ((80, 84), (15, 15)),
    ((86, 91), (17, 17)),
    ((92, 97), (18, 18)),
    ((98, 103), (19, 19)),
    ((116, 120), (22, 22)),
    ((122, 127), (24, 24)),
    ((128, 133), (25, 25)),
    ((134, 139), (26, 26)),
    ((140, 145), (27, 27)),
    ((158, 162), (30, 30)),
    ((164, 169), (32, 32)),
    ((170, 175), (33, 33)),
    ((176, 181), (34, 34)),
    ((182, 187), (35, 35)),
    ((188, 193), (36, 36)),
    ((206, 210), (39, 39)),
    ((212, 217), (41, 41)),
    ((218, 223), (42, 42)),
    ((224, 229), (43, 43)),
    ((230, 235), (44, 44)),
    ((236, 241), (45, 45)),
    ((242, 247), (46, 46)),
    ((260, 264), (49, 49)),
    ((266, 271), (51, 51)),
    ((272, 277), (52, 52)),
    ((278, 283), (53, 53)),
    ((284, 289), (54, 54)),
    ((290, 295), (55, 55)),
    ((296, 301), (56, 56)),
    ((302, 307), (57, 57)),
    ((308, 313), (58, 58)),
    ((326, 330), (61, 61)),
    ((332, 337), (63, 63)),
    ((338, 343), (64, 64)),
    ((344, 349), (65, 65)),
    ((350, 355), (66, 66)),
    ((356, 361), (67, 67)),
    ((362, 367), (68, 68)),
    ((368, 373), (69, 69)),
    ((374, 379), (70, 70)),
    ((392, 396), (75, 75)),
    ((398, 403), (77, 77)),
    ((404, 409), (78, 78)),
    ((410, 415), (79, 79)),
    ((416, 421), (80, 80)),
    ((422, 427), (81, 81)),
    ((428, 433), (82, 82)),
    ((434, 439), (83, 83)),
    ((440, 445), (84, 84)),
    ((458, 462), (89, 89)),
    ((464, 469), (91, 91)),
    ((470, 475), (92, 92)),
    ((476, 481), (93, 93)),
    ((482, 487), (94, 94)),
    ((488, 493), (95, 95)),
    ((494, 499), (96, 96)),
    ((500, 505), (97, 97)),
    ((506, 511), (98, 98)),
    ((512, 517), (99, 99)),
    ((530, 534), (102, 102)),
    ((536, 541), (104, 104)),
    ((542, 547), (105, 105)),
    ((548, 553), (106, 106)),
    ((554, 559), (107, 107)),
    ((560, 565), (108, 108)),
    ((566, 571), (109, 109)),
    ((572, 577), (110, 110)),
    ((578, 583), (111, 111)),
    ((584, 589), (112, 112)),
    ((602, 606), (115, 115)),
    ((608, 613), (117, 117)),
    ((614, 619), (118, 118)),
    ((620, 625), (119, 119)),
    ((626, 631), (120, 120)),
    ((644, 648), (123, 123)),
    ((650, 655), (125, 125)),
    ((656, 661), (126, 126)),
    ((662, 667), (127, 127)),
    ((668, 673), (128, 128)),
    ((674, 679), (129, 129)),
    ((680, 685), (130, 130)),
    ((698, 702), (133, 133)),
    ((704, 709), (135, 135)),
    ((710, 715), (136, 136)),
    ((716, 721), (137, 137)),
    ((722, 727), (138, 138)),
    ((728, 733), (139, 139)),
    ((734, 739), (140, 140)),
    ((740, 745), (141, 141)),
    ((758, 762), (146, 146)),
    ((764, 769), (148, 148)),
    ((770, 775), (149, 149)),
    ((776, 781), (150, 150)),
    ((782, 787), (151, 151)),
    ((788, 793), (152, 152)),
    ((794, 799), (153, 153)),
    ((800, 805), (154, 154)),
    ((806, 811), (155, 155)),
)
