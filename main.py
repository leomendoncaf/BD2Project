from database import Database
from avaliacao_crud import AvaliacaoCRUD
from cli import AvaliacaoCLI

db=Database("bolt://3.235.10.32:7687", "neo4j", "linens-member-complaints")

cli_db = AvaliacaoCRUD(db)

avalcli = AvaliacaoCLI(cli_db)
avalcli.run()

db.close()