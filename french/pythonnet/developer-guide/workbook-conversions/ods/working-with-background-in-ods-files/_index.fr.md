---
title: Travailler avec l'arrière-plan dans les fichiers ODS
type: docs
weight: 150
url: /fr/python-net/working-with-background-in-ods-files/
description: Comment travailler avec l'arrière-plan dans les fichiers ODS avec Aspose.Cells for Python via .NET API.
keywords: Python work with Background in ODS Files, Read Background Information from ODS file Pyton via NET, Add Colored Background to ODS file using Python via NET, Python via NET Add Graphic Background to ODS file.
---
##  **Contexte dans les fichiers ODS**

L’arrière-plan peut être ajouté aux feuilles dans les fichiers ODS. Le fond peut être soit un fond coloré, soit un fond graphique. L'arrière-plan n'est pas visible lorsque le fichier est ouvert, mais si le fichier est imprimé sous le numéro PDF, l'arrière-plan est visible dans le PDF généré. L'arrière-plan est également visible dans la boîte de dialogue d'aperçu avant impression.

Aspose.Cells for Python via .NET offre la possibilité de lire les informations d'arrière-plan et d'ajouter l'arrière-plan dans les fichiers ODS.

##  **Lire les informations générales du fichier ODS**

Aspose.Cells for Python via .NET fournit le[**OdsPageContexte**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) classe pour gérer l’arrière-plan dans les fichiers ODS. L'exemple de code suivant illustre l'utilisation de[**OdsPageContexte**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) classe en chargeant le[source ODS](90112030.ods) fichier et lire les informations de base. Veuillez consulter la sortie de la console générée par le code pour référence.

###  **Exemple de code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-ReadODSBackground-1.py" >}}

###  **Sortie console**

Type d'arrière-plan : Graphique

Position arrière-plan : CentreCentre

##  **Ajouter un arrière-plan coloré au fichier ODS**

Aspose.Cells for Python via .NET fournit le[**OdsPageContexte**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground)classe pour gérer l’arrière-plan dans les fichiers ODS. L'exemple de code suivant illustre l'utilisation de[**OdsPageBackground.color**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground/color/) propriété pour ajouter un arrière-plan de couleur au fichier ODS. Veuillez consulter le[sortie ODS](90112031.ods) fichier généré par le code pour référence.

###  **Exemple de code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-SetODSColoredBackground-1.py" >}}

##  **Ajouter un arrière-plan graphique au fichier ODS**

Aspose.Cells for Python via .NET fournit le[**OdsPageContexte**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground)classe pour gérer l’arrière-plan dans les fichiers ODS. L'exemple de code suivant illustre l'utilisation de[**OdsPageBackground.graphic_data**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground/graphic_data/)propriété pour ajouter un arrière-plan graphique au fichier ODS. Veuillez consulter le[sortie ODS](90112030.ods)fichier généré par le code pour référence.

###  **Exemple de code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-SetODSGraphicBackground-1.py" >}}
