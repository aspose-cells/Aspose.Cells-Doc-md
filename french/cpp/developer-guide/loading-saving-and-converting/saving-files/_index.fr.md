---
title: Enregistrement des Fichiers
type: docs
weight: 20
url: /fr/cpp/saving-files/
---

{{% alert color="primary" %}} 

Aspose.Cells permet de créer et d'enregistrer des fichiers, et de manipuler des fichiers existants. Cet article explique les différentes façons dont les fichiers peuvent être enregistrés.

{{% /alert %}} 
## **Différentes façons d'enregistrer des fichiers**
Aspose.Cells fournit le [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Microsoft Excel et fournit les méthodes nécessaires pour travailler avec les fichiers Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) fournit la méthode [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) utilisée pour enregistrer les fichiers Excel. La méthode [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) possède de nombreuses surcharges qui sont utilisées pour enregistrer les fichiers de différentes manières. Le format de fichier dans lequel le fichier est enregistré est décidé par l'énumération [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/).
## **Enregistrer le fichier à un emplacement quelconque**
Pour enregistrer des fichiers dans un emplacement de stockage, spécifiez le nom du fichier (complet avec le chemin de stockage) et le format de fichier souhaité (à partir de l'énumération [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)) lors de l'appel de la méthode [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) de l'objet [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation-new.cpp" >}}


## **Enregistrement du Fichier dans un Flux**
Pour enregistrer des fichiers dans un flux, créez un objet MemoryStream ou FileStream et enregistrez le fichier dans cet objet de flux en appelant la méthode [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) de l'objet [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). Spécifiez le format de fichier souhaité en utilisant l'énumération [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) lors de l'appel de la méthode [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/).



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream-new.cpp" >}}

## **Enregistrement du fichier au format PDF**
Pour enregistrer le contenu souhaité dans un fichier PDF en utilisant la bibliothèque Aspose.Cells for C++, créez un nouvel objet [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) ou construisez un objet [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) en lisant un fichier Excel existant, puis enregistrez le fichier au format PDF en appelant la méthode Save de l'objet [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). Lors de l'appel de la méthode Save, utilisez l'énumération [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) pour spécifier le format de fichier désiré.


{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToPdf-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
