---
title: Prise en charge des signatures numériques
type: docs
weight: 70
url: /fr/reportingservices/support-for-digital-signatures/
---
{{% alert color="primary" %}} 

Une signature numérique garantit qu'un classeur est valide et que personne ne l'a modifié. Joindre une signature numérique revient à sceller une enveloppe. Si une enveloppe arrive scellée, vous avez un certain niveau d'assurance que personne n'a altéré son contenu.

 Vous pouvez créer une signature numérique personnelle en utilisant le Microsoft Selfcert.exe ou tout autre outil, ou vous pouvez acheter une signature numérique. Pour signer une feuille de calcul, attachez une signature à vos classeurs une fois que vous avez créé une signature numérique.

 Aspose.Cells for Reporting Services prend en charge les signatures numériques.

{{% /alert %}} 
### **Travailler avec des signatures numériques**
#### **Formats Excel pris en charge pour les signatures numériques**
Aspose.Cells for Reporting Services prend en charge les signatures numériques lors de l'exportation vers les formats de fichier Excel 2007 et ODS.
#### **Configuration des signatures numériques**
 Le**Aspose.Cells.ReportingServices.xml** contient les informations de configuration et le texte d'une signature numérique dans le<DigitalSignature> étiquette:

- Lorsque DigitalSignature est désactivé, Aspose.Cells for Reporting Services désactive la fonctionnalité de signature numérique.
Par exemple:

{{< highlight "java" >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

- Lorsque la valeur de DigitalSignature est activée, Aspose.Cells.ReportingServices active la fonctionnalité de signature numérique.
Par exemple:

{{< highlight "java" >}}

 <DigitalSignature value="on">

{{< /highlight >}}

 Il y a quatre paramètres dans la section DigitalSignature. Ceux-ci sont :

- nom – Pointe vers un rapport nécessitant une signature numérique. Le rapport utilise un fichier PFX pour la signature numérique lorsque le paramètre est vide.
- pfxFilename – Pointe vers le fichier PFX. Le nom de fichier doit être un nom de fichier complet. Il ne peut pas être défini sur une valeur vide.
- pfxPwd – Définit le mot de passe. Il ne peut pas être laissé vide.
- but – Explique le but de la signature. Il peut être vide.
Par exemple:

{{< highlight "java" >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
