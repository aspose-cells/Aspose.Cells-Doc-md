---
title: Extensions Web  Modules complémentaires Office
type: docs
weight: 130
url: /fr/python-net/web-extensions-office-add-ins/
---

Les extensions Web étendent les applications Office et interagissent avec le contenu des documents Office. Les extensions Web ajoutent des fonctionnalités supplémentaires au client Office pour améliorer l'expérience utilisateur et la productivité.

Aspose.Cells pour Python via .NET offre également la possibilité de travailler avec des extensions web.

## **Ajouter une extension Web**

Vous pouvez ajouter des extensions Web (compléments Office) dans Excel en cliquant sur l'onglet **Insérer** puis en cliquant sur le lien **Magasin**/**Obtenir des compléments**. Dans la boîte de dialogue des compléments, recherchez le complément souhaité et ajoutez-le.

Aspose.Cells pour Python via .NET permet également d’ajouter des extensions web en utilisant les classes [**WebExtension**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextension) et [**WebExtensionTaskPane**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextensiontaskpane). Le code ci-dessous montre comment utiliser les classes [**WebExtension**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextension) et [**WebExtensionTaskPane**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextensiontaskpane) pour ajouter une extension web au fichier Excel. Veuillez consulter le fichier Excel de sortie ([output Excel file](89849869.xlsx)) généré par le code pour référence.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-WebExtension-Workbook-AddWebExtension-1.py" >}}

## **Accéder aux informations sur l'extension Web**

Aspose.Cells pour Python via .NET permet d’accéder aux informations des extensions web dans un fichier Excel. Le code suivant montre comment accéder aux informations des extensions web en chargeant le [fichier Excel exemple](89849870.xlsx). Consultez la sortie console générée par le code pour référence.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-WebExtension-Workbook-AccessWebExtensionInformation-1.py" >}}

### **Sortie console**

{{< highlight java >}}

Width: 350

IsVisible: True

IsLocked: False

DockState: right

StoreName: en-US

StoreType: OMEX

WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
