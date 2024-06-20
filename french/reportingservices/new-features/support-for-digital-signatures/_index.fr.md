---
title: Prise en charge des signatures numériques
type: docs
weight: 70
url: /fr/reportingservices/support-for-digital-signatures/
---

{{% alert color="primary" %}} 

Une signature numérique garantit qu'un classeur est valide et qu'aucune modification n'a été apportée. Attacher une signature numérique revient à sceller une enveloppe. Si une enveloppe arrive scellée, vous avez une certaine assurance que personne n'a altéré son contenu. 

Vous pouvez créer une signature numérique personnelle en utilisant Microsoft Selfcert.exe ou tout autre outil, ou vous pouvez en acheter une. Pour signer une feuille de calcul, attachez une signature à vos classeurs une fois que vous avez créé une signature numérique. 

Aspose.Cells for Reporting Services prend en charge les signatures numériques. 

{{% /alert %}} 
### **Travailler avec les signatures numériques**
#### **Formats Excel pris en charge pour les signatures numériques**
Aspose.Cells for Reporting Services prend en charge les signatures numériques lors de l'exportation vers les formats de fichier Excel 2007 et ODS.
#### **Configuration des signatures numériques**
The **Aspose.Cells.ReportingServices.xml** file holds the configuration information and text of a digital signature in the <DigitalSignature> tag:

- Lorsque DigitalSignature est désactivé, Aspose.Cells for Reporting Services désactive la fonctionnalité de signature numérique.
  Par exemple: 

{{< highlight java >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

- Lorsque la valeur de DigitalSignature est activée, Aspose.Cells.ReportingServices active la fonctionnalité de signature numérique.
  Par exemple: 

{{< highlight java >}}

 <DigitalSignature value="on">

{{< /highlight >}}

Il y a quatre paramètres dans la section DigitalSignature. Ce sont: 

- name - Pointe vers un rapport qui nécessite une signature numérique. Le rapport utilise un fichier PFX pour la signature numérique lorsque le paramètre est vide.
- pfxFilename - Pointe vers le fichier PFX. Le nom de fichier doit être un nom de fichier complet. Il ne peut pas être défini sur une valeur vide.
- pfxPwd - Définit le mot de passe. Il ne peut pas être laissé vide.
- purpose - Explique le but de la signature. Il peut être vide.
  Par exemple: 

{{< highlight java >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
