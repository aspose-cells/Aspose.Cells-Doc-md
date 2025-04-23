---
title: Vérifier si le projet VBA dans un classeur est signé
type: docs
weight: 70
url: /fr/net/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

Vous pouvez vérifier si votre projet VBA est signé ou non en utilisant Microsoft Excel via la commande de menu **Outils > Signatures numériques...** De même, vous pouvez le vérifier de manière programmatique en utilisant la propriété Aspose.Cells [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/issigned).

{{% /alert %}}

## **Vérifiez si le projet VBA dans un classeur est signé en C#**

Le code suivant charge le classeur et vérifie si son projet VBA est signé en utilisant la propriété [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/issigned). La propriété renverra **true** si le projet est signé sinon elle renverra **false**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaProjectSigned-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
