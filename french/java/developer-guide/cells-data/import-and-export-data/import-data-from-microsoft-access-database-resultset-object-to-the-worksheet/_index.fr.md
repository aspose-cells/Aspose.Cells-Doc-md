---
title: Importer des données de l'objet ResultSet de la base de données Access Microsoft dans la feuille de calcul
type: docs
weight: 200
url: /fr/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/
---
## **Scénarios d'utilisation possibles**
Aspose.Cells peut importer des données dans des feuilles de calcul à partir d'un objet ResultSet qui peut être créé à partir de n'importe quelle base de données. Toutefois, cet article crée spécifiquement un objet ResultSet à partir de la base de données Access Microsoft. Étant donné que le code est le même pour tous les types de bases de données, vous pouvez donc l'utiliser en général.
## **UCanAccess - Requis pour se connecter à la base de données Access Microsoft**
 Veuillez télécharger[UCanAccess](http://ucanaccess.sourceforge.net/site.html). Il inclut les fichiers JAR suivants. Ajoutez-les tous dans le classpath.

- ucanaccess-4.0.1.jar
- commons-lang-2.6.jar
- commons-logging-1.1.1.jar
- hsqldb.jar
- jackcess-2.1.6.jar

Pour plus d'aide, veuillez visiter ce lien Stack Overflow.

- [Ajouter manuellement les fichiers JAR à votre projet](https://stackoverflow.com/questions/21955256/manipulating-an-access-database-from-java-without-odbc/21955257#21955257)
## **Exemple de fichier de base de données Access Microsoft Access 2016 utilisé dans l'exemple de code**
L'exemple de fichier de base de données Access 2016 Microsoft suivant a été utilisé dans l'exemple de code. Vous pouvez utiliser n'importe quel fichier de base de données ou créer le vôtre.

- [Étudiants.accdb](48496712.accdb)

La capture d'écran suivante montre le fichier de base de données lorsqu'il est ouvert dans Microsoft Access 2016.

![tâche : image_autre_texte](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_1.png)
## **Importer des données à partir de l'objet ResultSet de la base de données Access Microsoft dans la feuille de calcul.**
 L'exemple de code suivant exécute une requête SQL à partir de la base de données Access Microsoft et crée un objet ResultSet. Ensuite, il importe les données de l'objet ResultSet dans la feuille de calcul à l'aide[Feuille de calcul.getCells().importResultSet()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importResultSet\(java.sql.ResultSet,%20int,%20int,%20boolean\)) méthode. La première fois, il utilise des indices de ligne et de colonne, puis il utilise le nom de la cellule pour importer des données dans la feuille de calcul. Enfin, il enregistre le classeur en tant que[Fichier Excel de sortie](48496713.xlsx). La capture d'écran montre l'effet de l'exemple de code sur le fichier Excel de sortie pour une référence.

![tâche : image_autre_texte](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_2.png)
## **Exemple de code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportDataFromMicrosoftAccessDatabaseResultSetObjectToWorksheet.java" >}}
