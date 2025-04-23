---
title: Enregistrement des Fichiers
type: docs
weight: 20
url: /fr/go-cpp/saving-files/
---

{{% alert color="primary" %}}

Aspose.Cells permet de créer et d'enregistrer des fichiers ainsi que de manipuler les fichiers existants. Cet article explique les différentes façons de sauvegarder les fichiers.

{{% /alert %}}

## **Différentes façons d'enregistrer des fichiers**

Aspose.Cells fournit la classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/), qui représente un fichier Microsoft Excel et offre les méthodes nécessaires pour travailler avec des fichiers Excel. La classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) fournit la méthode [Save](https://reference.aspose.com/cells/go-cpp/workbook/save/) utilisée pour enregistrer des fichiers Excel. La méthode [Save](https://reference.aspose.com/cells/go-cpp/workbook/save/) possède de nombreuses surcharges permettant de sauvegarder des fichiers de différentes manières. Le format de fichier dans lequel le fichier est sauvegardé est déterminé par l’énumération [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/).

## **Enregistrer le fichier à un emplacement quelconque**

Pour sauvegarder des fichiers dans un emplacement de stockage, spécifiez le nom du fichier (avec le chemin de stockage complet) et le format de fichier souhaité (désigné par l’énumération [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/)) lors de l’appel à la méthode [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/) de l’objet [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToSomeLocation.go" >}}

## **Enregistrement du Fichier dans un Flux**

Pour sauvegarder des fichiers vers un flux, créez un objet MemoryStream ou FileStream et sauvegardez le fichier dans cet objet flux en appelant la méthode [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/) de l’objet [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/). Spécifiez le format de fichier souhaité en utilisant l’énumération [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/) lors de l’appel à la méthode [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_saveFormat/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToStream.go" >}}

## **Enregistrement du fichier au format PDF**

Pour sauvegarder le contenu souhaité en fichier PDF en utilisant la bibliothèque Aspose.Cells for Go via C++, créez un nouveau [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) ou construisez un [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) en lisant un fichier Excel existant, puis en [enregistrant](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveOptions/) le fichier au format PDF en appelant la méthode Save du objet [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/). Lors de l’appel à la méthode Save, utilisez l’énumération [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/) pour spécifier le format de fichier souhaité.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToPdf.go" >}}
