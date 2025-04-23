---
title: Détermination si la licence est chargée avec succès
type: docs
weight: 260
url: /fr/net/determining-if-the-license-is-loaded-successfully/
description: Apprenez comment détecter si la licence est chargée avec succès via les API Aspose.Cells for NET.
keywords: Comment détecter si la licence est chargée avec succès en C#, Déterminer si la licence est chargée avec succès en utilisant C#, Vérifier si la licence est chargée avec succès via C#, vérifier le statut de la licence.
---

{{% alert color="primary" %}}

Aspose.Cells fournit [**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) propriété que vous pouvez utiliser pour déterminer si la licence est chargée avec succès ou non. Si vous accédez à cette propriété avant de définir la licence, elle renverra **false** et si vous appelez cette propriété après avoir défini la licence, elle renverra **true** indiquant que la licence a été chargée avec succès.

{{% /alert %}}

## Code C# pour déterminer si la licence est chargée avec succès

Le code suivant accède à la propriété [**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) avant de définir une licence et retourne **false**. Ensuite, il charge la licence et accède de nouveau à la propriété qui retourne maintenant **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

## **Sortie console**

Voici la sortie de la console (debug) du code d'exemple ci-dessus

{{< highlight java >}}

False

True

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
