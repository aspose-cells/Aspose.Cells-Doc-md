---
title: Convertir un fichier Excel au format PDF compatible avec PDFA 1a
type: docs
weight: 80
url: /fr/java/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---

## **Scénarios d'utilisation possibles**

PDF/A est une variante unique du format PDF conçue pour la préservation à long terme des documents. PDF/A est une version normalisée par l'ISO du format de document portable (PDF), qui est un format d'archivage PDF qui intègre toutes les polices utilisées dans le document dans le fichier PDF. PDF/A diffère du PDF en interdisant des fonctionnalités telles que la liaison des polices (par opposition à l'intégration des polices) et le chiffrement. Aspose.Cells vous permet d'enregistrer les fichiers Excel au format PDF/A compatible (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab et PDF/A-3u sont pris en charge). Ce sujet décrit comment enregistrer le classeur Excel au format PDF/A compatible (PDF/A-1a) fichier PDF.

## **Convertir le fichier Excel au format PDF compatible avec le PDF/A-1a**

Les développeurs peuvent utiliser la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) pour définir différentes propriétés pour la conversion. Le fait de définir différentes propriétés de la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) vous donne le contrôle sur les paramètres d'impression, de police, de sécurité et de compression pour le fichier PDF de sortie. La propriété la plus importante est [PdfSaveOptions.Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance) qui vous permet de sauvegarder les fichiers Excel au format PDF/A conforme.

Le code d'exemple suivant explique comment convertir le fichier Excel au format PDF compatible avec le PDF/A-1a. Veuillez consulter son [PDF de sortie](outputCompliancePdfA1a.pdf) ainsi qu'une capture d'écran à titre de référence.

## **Capture d'écran**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.java" >}}
