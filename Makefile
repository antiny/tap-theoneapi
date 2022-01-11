run_tap:
	poetry run tap-theoneapi --config config.json --catalog catalog.json | target-json > state.json

run_tap_config:
	poetry run tap-theoneapi --config config.json --discover > ./catalog.json

run_meltano:
	meltano elt tap-theoneapi target-jsonl
