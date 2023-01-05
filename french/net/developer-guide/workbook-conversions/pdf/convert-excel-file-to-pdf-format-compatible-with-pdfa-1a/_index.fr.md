---
title: Convertir le fichier Excel au format PDF compatible avec PDFA-1a
type: docs
weight: 130
url: /fr/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---
## **Scénarios d'utilisation possibles**

PDF/A est une saveur unique de PDF conçue pour la conservation à long terme des documents. PDF/A est une version normalisée ISO du Portable Document Format (PDF) qui est un format d'archivage de PDF qui intègre toutes les polices utilisées dans le document dans le fichier PDF. PDF/A diffère de PDF en interdisant des fonctionnalités telles que la liaison de polices (par opposition à l'incorporation de polices) et le cryptage. Aspose.Cells vous permet d'enregistrer les fichiers Excel dans des fichiers PDF/A conformes à la norme PDF (PdfA1a et PdfA1b sont pris en charge). Cette rubrique décrit comment enregistrer le classeur Excel dans un fichier PDF/A conforme (PdfA1a) PDF.

## **Convertir le fichier Excel au format PDF compatible avec PDFA-1a**

Les développeurs peuvent utiliser le**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**class pour définir différents attributs pour la conversion. Définition de différentes propriétés du**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**La classe vous permet de contrôler les paramètres d'impression, de police, de sécurité et de compression pour la sortie PDF. La propriété la plus importante est**[PdfSaveOptions.Compliance](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**qui vous permet d'enregistrer les fichiers Excel dans des fichiers PDF/A conformes à la norme PDF.

L'exemple de code suivant explique comment convertir un fichier Excel au format PDF compatible avec PDFA-1a. Veuillez voir son[sortie PDF](outputCompliancePdfA1a.pdf) ainsi que la capture d'écran pour référence.

## **Capture d'écran**

![tâche : image_autre_texte](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.cs" >}}
