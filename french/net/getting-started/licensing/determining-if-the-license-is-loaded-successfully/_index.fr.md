---
title: Déterminer si la licence est chargée avec succès
type: docs
weight: 260
url: /fr/net/determining-if-the-license-is-loaded-successfully/
---
{{% alert color="primary" %}}

 Aspose.Cells fournit[**Workbook.IsLicensedClasser.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) propriété que vous pouvez utiliser pour déterminer si la licence est chargée avec succès ou non. Si vous accédez à cette propriété avant de définir la licence, elle renverra**faux**et si vous appelez cette propriété après avoir défini la licence, elle renverra**vrai** indiquant que la licence a été chargée avec succès.

{{% /alert %}}

## Code C# pour déterminer si la licence est chargée avec succès

 Le code suivant accède au[**Workbook.IsLicensedClasser.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) propriété avant de définir une licence et il retourne**faux** . Ensuite, il charge la licence et accède à nouveau à la propriété qui renvoie maintenant**vrai**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

## **Sortie console**

Voici la sortie console (débogage) de l'exemple de code ci-dessus

{{< highlight "java" >}}

False

True

{{< /highlight >}}
