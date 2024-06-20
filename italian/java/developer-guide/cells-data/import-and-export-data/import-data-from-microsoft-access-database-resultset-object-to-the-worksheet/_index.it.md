---
title: Importazione dei Dati dall oggetto ResultSet del Database di Microsoft Access nel Foglio di Lavoro
type: docs
weight: 200
url: /it/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/
---

## **Possibili Scenari di Utilizzo**
Aspose.Cells può importare dati nei fogli di lavoro dall'oggetto ResultSet che può essere creato da qualsiasi database. Tuttavia, questo articolo crea specificamente un oggetto ResultSet dal Database di Microsoft Access. Poiché il codice è lo stesso per tutti i tipi di database, è possibile utilizzarlo in generale.
## **UCanAccess - Necessario per Connettersi al Database di Microsoft Access**
Si prega di scaricare [UCanAccess](http://ucanaccess.sourceforge.net/site.html). Include i seguenti file JAR. Aggiungili tutti nel classpath.

- ucanaccess-4.0.1.jar
- commons-lang-2.6.jar
- commons-logging-1.1.1.jar
- hsqldb.jar
- jackcess-2.1.6.jar

Per ulteriore assistenza, visita questo link di Stack Overflow.

- [Aggiungere manualmente i JAR al tuo progetto](https://stackoverflow.com/questions/21955256/manipulating-an-access-database-from-java-without-odbc/21955257#21955257)
## **File di database di esempio Microsoft Access 2016 utilizzato nel codice di esempio**
Il seguente file di database di esempio Microsoft Access 2016 è stato utilizzato nel codice di esempio. Puoi utilizzare qualsiasi file di database o crearne uno.

- [Students.accdb](48496712.accdb)

La seguente schermata mostra il file di database quando aperto in Microsoft Access 2016.

![todo:image_alt_text](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_1.png)
## **Importare i dati dall'oggetto ResultSet del database di Microsoft Access nel foglio di lavoro.**
Il seguente codice di esempio esegue la query SQL dal database di Microsoft Access e crea un oggetto ResultSet. Poi importa i dati dall'oggetto ResultSet nel foglio di lavoro usando il metodo [Worksheet.getCells().importResultSet()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importResultSet\(java.sql.ResultSet,%20int,%20int,%20boolean\)). La prima volta utilizza gli indici di riga e colonna e poi utilizza il nome della cella per importare i dati nel foglio di lavoro. Infine, salva il workbook come un [File Excel di output](48496713.xlsx). La schermata mostra l'effetto del codice di esempio sul file Excel di output per riferimento.

![todo:image_alt_text](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_2.png)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportDataFromMicrosoftAccessDatabaseResultSetObjectToWorksheet.java" >}}
