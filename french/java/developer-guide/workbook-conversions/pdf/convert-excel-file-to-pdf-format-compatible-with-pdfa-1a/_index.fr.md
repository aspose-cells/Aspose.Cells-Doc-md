---
title: Convertir un fichier Excel au format PDF compatible avec PDFA-1a
type: docs
weight: 80
url: /fr/java/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---
## **Scénarios d'utilisation possibles**

PDF/A est une version unique de PDF conçue pour la conservation à long terme des documents. PDF/A est une version normalisée ISO du Portable Document Format (PDF) qui est un format d'archivage de PDF qui intègre toutes les polices utilisées dans le document dans le fichier PDF. Le PDF/A diffère du PDF en interdisant des fonctionnalités telles que la liaison de polices (par opposition à l'incorporation de polices) et le cryptage. Aspose.Cells vous permet d'enregistrer les fichiers Excel dans des fichiers PDF compatibles PDF/A (PdfA1a et PdfA1b sont pris en charge). Cette rubrique décrit comment enregistrer le classeur Excel dans un fichier PDF compatible PDF/A (PdfA1a).

## **Convertir un fichier Excel au format PDF compatible avec PDFA-1a**

Les développeurs peuvent utiliser le**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**class pour définir différents attributs pour la conversion. Définition de différentes propriétés du**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**La classe vous permet de contrôler les paramètres d'impression, de police, de sécurité et de compression du PDF de sortie. La propriété la plus importante est**[PdfSaveOptions.Compliance](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance)**qui vous permet d'enregistrer les fichiers Excel dans des fichiers PDF compatibles PDF/A.

 L'exemple de code suivant explique comment convertir un fichier Excel au format PDF compatible avec PDFA-1a. Veuillez voir son[PDF de sortie](outputCompliancePdfA1a.pdf) ainsi qu'une capture d'écran pour référence.

## **Capture d'écran**

![tâche : image_autre_texte](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.java" >}}
