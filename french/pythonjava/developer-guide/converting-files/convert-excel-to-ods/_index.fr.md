---
title: Convertir Excel en ODS
type: docs
weight: 40
url: /fr/python-java/convert-excel-to-ods/
---
## **Convertir Excel en ODS**
Les fichiers ODS sont créés par le programme Calc qui fait partie de la suite Apache OpenOffice. Les fichiers ODS stockent des données organisées en lignes et en colonnes et sont formatés à l'aide de la norme basée sur XML OASIS OpenDocument.

Aspose.Cells for Python via Java prend en charge les fichiers ODS fonctionnels. Les exemples suivants illustrent la conversion d'Excel en fichier ODS.
### **Conversion directe**
Le moyen le plus simple de convertir un fichier Excel en ODS est de charger le classeur et de l'enregistrer en passant[SaveFormat.ODS](https://reference.aspose.com/cells/python/asposecells.api/saveformat#ODS) comme deuxième paramètre de la[Classeur.save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20int\)) méthode.

L'extrait de code suivant a démontré la conversion d'Excel directement en ODS

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToODSFiles.py" >}}
### **Enregistrez le document ODS dans les spécifications ODF 1.1 ou 1.2**
Aspose.Cells for Python via Java prend en charge l'enregistrement des fichiers ODS dans les spécifications ODF 1.1 et ODF 1.2. Pour cela, le API fournit[OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) propriété. Définir cette propriété sur**vrai** enregistrera le fichier avec la spécification ODF 1.1. La valeur par défaut de[OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) est**faux**, de sorte que le fichier ODS enregistré sans paramètres spéciaux est enregistré avec la spécification ODF 1.2.

L'extrait de code suivant illustre l'enregistrement des fichiers ODS avec les spécifications ODF 1.1 et 1.2.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-SaveODSFilesWithSpecifications.py" >}}
