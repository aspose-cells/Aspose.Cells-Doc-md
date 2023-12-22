---
title: Déterminer si la licence est chargée avec succès
type: docs
weight: 260
url: /fr/net/determining-if-the-license-is-loaded-successfully/
description: Découvrez comment détecter si la licence est chargée avec succès via les API Aspose.Cells pour NET.
keywords: How to Detect if the License is loaded successfully in C#, Determine if the License is loaded successfully using C#, Check if the License is loaded successfully via C#, check the status of license.
---
{{% alert color="primary" %}}

 Aspose.Cells fournit[**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) propriété que vous pouvez utiliser pour déterminer si la licence est chargée avec succès ou non. Si vous accédez à cette propriété avant de définir la licence, elle renverra**FAUX** et si vous appelez cette propriété après avoir défini la licence, elle reviendra**vrai** indiquant que la licence a été chargée avec succès.

{{% /alert %}}

##  Code C# pour déterminer si la licence est chargée avec succès

 Le code suivant accède au[**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed)propriété avant de définir une licence et elle renvoie *false**. Ensuite, il charge la licence et accède à nouveau à la propriété qui renvoie désormais *true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

##  **Sortie console**

Voici la sortie console (débogage) de l'exemple de code ci-dessus

{{< highlight "java" >}}

False

True

{{< /highlight >}}
