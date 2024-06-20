---
title: Importer des données depuis l objet ResultSet de la base de données Microsoft Access vers la feuille de calcul
type: docs
weight: 200
url: /fr/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/
---

## **Scénarios d'utilisation possibles**
Aspose.Cells peut importer des données dans des feuilles de calcul à partir de l'objet ResultSet qui peut être créé à partir de n'importe quelle base de données. Cependant, cet article crée spécifiquement un objet ResultSet à partir de la base de données Microsoft Access. Étant donné que le code est le même pour tous les types de bases de données, vous pouvez l'utiliser de manière générale.
## **UCanAccess - Nécessaire pour se connecter à une base de données Microsoft Access**
Veuillez télécharger [UCanAccess](http://ucanaccess.sourceforge.net/site.html). Il inclut les fichiers JAR suivants. Ajoutez-les tous dans le chemin de classe.

- ucanaccess-4.0.1.jar
- commons-lang-2.6.jar
- commons-logging-1.1.1.jar
- hsqldb.jar
- jackcess-2.1.6.jar

Pour plus d'aide, veuillez visiter ce lien Stack Overflow.

- [Ajout manuel des JARs à votre projet](https://stackoverflow.com/questions/21955256/manipulating-an-access-database-from-java-without-odbc/21955257#21955257)
## **Fichier de base de données Microsoft Access 2016 d'exemple utilisé dans le code d'exemple**
Le fichier de base de données Microsoft Access 2016 d'exemple suivant a été utilisé dans le code d'exemple. Vous pouvez utiliser n'importe quel fichier de base de données ou en créer un.

- [Students.accdb](48496712.accdb)

La capture d'écran suivante montre le fichier de base de données lorsqu'il est ouvert dans Microsoft Access 2016.

![todo:image_alt_text](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_1.png)
## **Importer des données depuis l'objet ResultSet de la base de données Microsoft Access vers la feuille de calcul.**
Le code d'exemple suivant exécute une requête SQL à partir de la base de données Microsoft Access et crée un objet ResultSet. Ensuite, il importe des données depuis l'objet ResultSet dans la feuille de calcul en utilisant la méthode [Worksheet.getCells().importResultSet()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importResultSet\(java.sql.ResultSet,%20int,%20int,%20boolean\)). La première fois, il utilise des indices de lignes et de colonnes, puis il utilise le nom de la cellule pour importer des données dans la feuille de calcul. Enfin, il enregistre le classeur en tant que [Fichier Excel en sortie](48496713.xlsx). La capture d'écran montre l'effet du code d'exemple sur le fichier Excel de sortie pour une référence.

![todo:image_alt_text](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_2.png)
## **Code d'exemple**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportDataFromMicrosoftAccessDatabaseResultSetObjectToWorksheet.java" >}}
