---
title: Convertir Excel en ODS
type: docs
weight: 40
url: /fr/python-java/convert-excel-to-ods/
---

## **Convertir Excel en ODS**
Les fichiers ODS sont créés par le programme Calc, qui fait partie de la suite Apache OpenOffice. Les fichiers ODS stockent des données organisées en lignes et colonnes et sont formatés à l'aide de la norme XML OASIS OpenDocument.

Aspose.Cells pour Python via Java prend en charge le travail avec les fichiers ODS. Les exemples suivants montrent comment convertir Excel en un fichier ODS.
### **Conversion directe**
La manière la plus simple de convertir un fichier Excel en ODS est de charger le classeur et de l'enregistrer en passant [SaveFormat.ODS](https://reference.aspose.com/cells/python/asposecells.api/saveformat#ODS) comme deuxième paramètre de la méthode [Workbook.save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20int\)).

Le snippet de code suivant a démontré la conversion directe d'Excel en ODS

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToODSFiles.py" >}}
### **Enregistrer le document ODS dans les spécifications ODF 1.1 ou 1.2**
Aspose.Cells pour Python via Java prend en charge l'enregistrement de fichiers ODS dans les spécifications ODF 1.1 et ODF 1.2. Pour cela, l'API fournit la propriété [OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11). Définir cette propriété sur **true** enregistrera le fichier avec la spécification ODF 1.1. La valeur par défaut de [OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) est **false**, donc le fichier ODS enregistré sans réglages spéciaux est enregistré avec la spécification ODF 1.2.

Le snippet de code suivant a démontré l'enregistrement des fichiers ODS avec les spécifications ODF 1.1 et 1.2.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-SaveODSFilesWithSpecifications.py" >}}
