run-db:
	docker run --name heru_container -p 5432:5432 -e POSTGRES_PASSWORD=password -e POSTGRES_USER=postgres -e POSTGRES_DB=heru -d postgres