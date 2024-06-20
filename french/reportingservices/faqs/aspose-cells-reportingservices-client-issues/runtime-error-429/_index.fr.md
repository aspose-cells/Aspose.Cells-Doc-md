---
title: Erreur d exécution 429
type: docs
weight: 60
url: /fr/reportingservices/runtime-error-429/
---

##### **Description**
Erreur d'exécution : '429' 
Le composant ActiveX ne peut pas créer l'objet 
La ligne causant l'erreur est : 
Set AsposeClientTools = CreateObject("Aspose.Cells.ReportingServices.Client.AsposeClient"). 
##### **Solution**
{{% alert color="primary" %}} 

Réenregistrez **Aspose.Cells.ReportingServices.Client.dll** en utilisant l'utilitaire **Regasm.exe** : 

1. Exécutez cmd.exe en tant qu'administrateur.
1. cd $(Aspose.Cells for Reporting Services installation folder).
1. Exécutez **regasm.exe** pour enregistrer **Aspose.Cells.ReportingServices.Client.dll** manuellement. 

{{< highlight java >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm  Aspose.Cells.ReportingServices.Client.dll  /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase

{{< /highlight >}}

Veuillez vérifier l'environnement d'exécution de votre système. Par exemple : 

- Si votre Microsoft Office est x64, exécutez la commande 

{{< highlight java >}}

 @: ...%WINDIR%\Microsoft.NET\Framework64\v2.0.50727\regasm.exe

{{< /highlight >}}

- Si votre Microsoft Office est x86, exécutez la commande 

{{< highlight java >}}

 @: ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm.exe

{{< /highlight >}}

Veuillez vous référer à l'exemple/commande suivant :

{{< highlight java >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm "C:\Program Files (x86)\Aspose\Aspose.Cells for Reporting Services\Bin\Aspose.Cells.ReportingServices.Client.dll" /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase 

{{< /highlight >}}

{{% /alert %}}
