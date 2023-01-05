---
title: Copier des lignes et des colonnes dans Jython
type: docs
weight: 30
url: /fr/java/copying-rows-and-columns-in-jython/
---
## **Aspose.Cells - Copier des lignes et des colonnes**
 Pour joindre des documents à l'aide de**Aspose.Cells Java pour Jython**. Ici vous pouvez voir un exemple de code.

**Code Jython**

{{< highlight "java" >}}

 à partir des paramètres d'importation de cellules aspose

à partir de com.aspose.cells importer le classeur

classe LignesEtColonnes :

 définitivement__initialiser__(soi):



 dataDir = Settings.dataDir + 'TravaillerAvecLignesEtColonnes/LignesEtColonnes'



 # Copier des lignes

 self.copy_rows()

 # Copier des colonnes

 self.copy_columns()



 def copy_rows(dataDir):

 dataDir = Settings.dataDir + 'TravaillerAvecRowsAndColumns/RowsAndColumns/'

 # Instanciation d'un objet Workbook par le chemin du fichier Excel

 classeur = classeur(dataDir + 'Book1.xls')

 Accéder à la première feuille de calcul du fichier Excel

 feuille de calcul = classeur.getWorksheets().get(0)

 # Copiez la deuxième ligne avec les données, les mises en forme, les images et les objets de dessin

 # à la 12e ligne de la feuille de calcul.

 feuille de calcul.getCells().copyRow(feuille de calcul.getCells(),1,11)

 # Enregistrement du fichier Excel modifié au format par défaut (c'est-à-dire Excel 2003)

 workbook.save(dataDir + "Copy Rows.xls")

 print "Copier les lignes avec succès."



 def copy_columns(dataDir):

 dataDir = Settings.dataDir + 'TravaillerAvecRowsAndColumns/RowsAndColumns/'

 # Instanciation d'un objet Workbook par le chemin du fichier Excel

 classeur = classeur()

 Accéder à la première feuille de calcul du fichier Excel

 feuille de calcul = classeur.getWorksheets().get(0)

 # Mettez des données dans les lignes d'en-tête (A1:A4)

 je = 0

 alors que je< 5:

            worksheet.getCells().get(i, 0).setValue("Header Row #i")






        # Put some detail data (A5:A999)

        i = 5

        while i < 1000:

            worksheet.getCells().get(i, 0).setValue("Detail Row #i")



        # Create another Workbook.

        workbook1 = Workbook()

        # Get the first worksheet in the book.

        worksheet1 = workbook1.getWorksheets().get(0)

        # Copy the first column from the first worksheet of the first workbook into

        # the first worksheet of the second workbook.

        worksheet1.getCells().copyColumn(worksheet.getCells(),0,2)

        # Autofit the column.

        worksheet1.autoFitColumn(2)

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Copy Columns.xls")

        print "Copy Columns Successfully." 




if __name__ == '__main__':        

    RowsAndColumns()

{{< /highlight >}}
## **Télécharger le code d'exécution**
 Télécharger**Joindre des documents (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)
