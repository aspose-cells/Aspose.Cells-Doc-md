---
title: Convertir un fichier Excel au format PDF compatible avec PDFA 1a
type: docs
weight: 130
url: /fr/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---

## **Scénarios d'utilisation possibles**

PDF/A est une variante unique du format PDF conçue pour la préservation à long terme des documents. PDF/A est une version normalisée par l'ISO du format de document portable (PDF), qui est un format d'archivage PDF qui intègre toutes les polices utilisées dans le document dans le fichier PDF. PDF/A diffère du PDF en interdisant des fonctionnalités telles que la liaison des polices (par opposition à l'intégration des polices) et le chiffrement. Aspose.Cells vous permet d'enregistrer les fichiers Excel au format PDF/A compatible (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab et PDF/A-3u sont pris en charge). Ce sujet décrit comment enregistrer le classeur Excel au format PDF/A compatible (PDF/A-1a) fichier PDF.

## **Convertir le fichier Excel au format PDF Compatible avec PDF/A-1a**

Les développeurs peuvent utiliser la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) pour définir différentes attributs pour la conversion. Définir différentes propriétés de la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) vous donne le contrôle sur les paramètres d'impression, de police, de sécurité et de compression pour le PDF en sortie. La propriété la plus importante est [**PdfSaveOptions.Compliance**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance) qui vous permet de sauvegarder les fichiers Excel au format PDF/A conforme.

Le code d'exemple suivant explique comment convertir le fichier Excel au format PDF compatible avec PDF/A-1a. Veuillez consulter son [PDF de sortie](outputCompliancePdfA1a.pdf) ainsi que la capture d'écran pour référence.

## **Capture d'écran**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.cs" >}}
{{< app/cells/assistant language="csharp" >}}
