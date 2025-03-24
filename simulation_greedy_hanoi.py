import simulator.simulation_hanoi as simhanoi

# Load initial and sequence states
initial_state = simhanoi.load_configuration("./greedy_initial_state.json")
sequence = simhanoi.load_configuration("./greedy_sequence.json")

simhanoi.main(initial_state, sequence)
