---
title: Importa i dati dall'oggetto ResultSet del database di Microsoft Access nel foglio di lavoro
type: docs
weight: 200
url: /it/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/
---
## **Possibili scenari di utilizzo**
Aspose.Cells può importare dati in fogli di lavoro dall'oggetto ResultSet che può essere creato da qualsiasi database. Questo articolo tuttavia crea specificamente un oggetto ResultSet dal database di Microsoft Access. Poiché il codice è lo stesso per tutti i tipi di database, è possibile utilizzarlo in generale.
## **UCanAccess: necessario per connettersi al database di Microsoft Access**
 Si prega di scaricare[UCanAccess](http://ucanaccess.sourceforge.net/site.html). Include i seguenti file JAR. Aggiungili tutti nel classpath.

- ucanaccess-4.0.1.jar
- commons-lang-2.6.jar
- commons-logging-1.1.1.jar
- hsqldb.jar
- jackcess-2.1.6.jar

Per ulteriore assistenza, visitare questo collegamento Stack Overflow.

- [Aggiungere manualmente i JAR al tuo progetto](https://stackoverflow.com/questions/21955256/manipulating-an-access-database-from-java-without-odbc/21955257#21955257)
## **Esempio di file di database di Microsoft Access 2016 utilizzato all'interno del codice di esempio**
Il seguente file di database Microsoft Access 2016 di esempio è stato utilizzato all'interno del codice di esempio. Puoi utilizzare qualsiasi file di database o crearne uno tuo.

- [Studenti.accdb](48496712.accdb)

Lo screenshot seguente mostra il file del database quando viene aperto in Microsoft Access 2016.

![cose da fare:immagine_alt_testo](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_1.png)
## **Importa i dati dall'oggetto ResultSet del database di Microsoft Access nel foglio di lavoro.**
 Il seguente codice di esempio esegue la query SQL dal database di Microsoft Access e crea un oggetto ResultSet. Quindi importa i dati dall'oggetto ResultSet nel foglio di lavoro utilizzando[Foglio di lavoro.getCells().importResultSet()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importResultSet\(java.sql.ResultSet,%20int,%20int,%20boolean\)) metodo. La prima volta utilizza gli indici di riga e colonna e quindi utilizza il nome della cella per importare i dati nel foglio di lavoro. Infine, salva la cartella di lavoro come file[File Excel di output](48496713.xlsx). Lo screenshot mostra l'effetto del codice di esempio sul file Excel di output come riferimento.

![cose da fare:immagine_alt_testo](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_2.png)
## **Codice di esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportDataFromMicrosoftAccessDatabaseResultSetObjectToWorksheet.java" >}}
