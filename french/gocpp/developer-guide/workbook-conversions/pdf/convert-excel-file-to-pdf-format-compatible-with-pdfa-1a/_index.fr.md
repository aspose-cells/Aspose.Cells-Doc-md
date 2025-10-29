---
title: Convertir un fichier Excel en format PDF compatible avec PDFA 1a avec Golang via C++
linktitle: Convertir un fichier Excel au format PDF compatible avec PDFA 1a
type: docs
weight: 130
url: /fr/go-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: Apprenez comment convertir des fichiers Excel en format PDF/PDF/A 1a conforme en utilisant Aspose.Cells avec Golang via C++.
---

## **Scénarios d'utilisation possibles**

PDF/A est une version spécifique de PDF conçue pour la conservation à long terme des documents. PDF/A est une version normalisée par ISO du format Portable Document (PDF) qui embed tous les polices utilisées dans le document au sein du fichier PDF. PDF/A diffère de PDF en interdisant certaines fonctionnalités, telles que la liaison de polices (contrairement à l’incorporation de polices) et le chiffrement. Aspose.Cells vous permet d'enregistrer les fichiers Excel en fichiers PDF conformes à PDF/A (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab et PDF/A-3u sont supportés). Ce sujet décrit comment sauvegarder un classeur Excel au format PDF/A conforme (PDF/A-1a).

## **Convertir le fichier Excel au format PDF Compatible avec PDF/A-1a**

Les développeurs peuvent utiliser la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) pour définir différents attributs pour la conversion. La définition de différentes propriétés de la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) vous donne le contrôle sur les paramètres d'impression, de police, de sécurité et de compression pour le PDF de sortie. La propriété la plus importante est [**PdfSaveOptions.GetCompliance()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getcompliance/) qui vous permet d'enregistrer les fichiers Excel au format PDF/A conforme.

Le code d'exemple suivant explique comment convertir le fichier Excel au format PDF compatible avec PDF/A-1a. Veuillez consulter son [PDF de sortie](outputCompliancePdfA1a.pdf) ainsi que la capture d'écran pour référence.

## **Capture d'écran**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelFileToPdfFormatCompatibleWithPdfa1a.go" >}}
