---
title: Fichier de licence ne fonctionne plus
type: docs
weight: 60
url: /fr/net/license-file-not-working-anymore/
---

## **Symptôme**

Parfois, les utilisateurs sont frustrés car leurs fichiers de licence ne fonctionnent plus lorsqu'ils déplacent / publient leur(s) projet(s) web sur un nouveau serveur. Ils sont mécontents car leurs fichiers de licence fonctionnaient correctement sur leur précédent (ancien) serveur, mais maintenant ils obtiennent un avertissement de copyright d'évaluation supplémentaire sur la feuille de travail (lorsqu'ils génèrent des rapports en utilisant le composant) dans le nouvel environnement du serveur.

### **Un scénario**

"Nous utilisons Aspose.Cells sur notre projet web ASP.NET pour générer / manipuler des rapports Excel, nous avons une licence valide que nous utilisons. Il y a quelques jours, nous avons déplacé le site web vers un nouveau serveur ; il n'y a eu aucune mise à niveau ou modification quelconque, nous avons vérifié et simplement déplacé chaque fichier sur le nouveau serveur, y compris le fichier Aspose.Cells.dll et les fichiers .lic connexes. Maintenant, lorsque nous essayons de générer des rapports Excel dans le nouvel environnement du serveur, nous obtenons une feuille avec un avertissement de copyright d'évaluation sur nos rapports. Nous avons essayé de télécharger et d'installer un nouveau fichier de licence à partir de la section My Orders du site, mais cela n'a pas du tout résolu le problème. Pour votre information, nous mettons en œuvre la licence en plaçant le fichier Aspose.Cells.lic dans le dossier bin du site ainsi que le fichier du composant Aspose.Cells.dll, qui, comme je l'ai mentionné, fonctionnait sans problème sur l'ancien serveur."

### **Solution**

Aspose dispose d'un mécanisme de licence propre et fiable. Généralement, le problème doit être lié à un problème de déploiement. Si un fichier de licence fonctionne bien (sur un serveur), il devrait tout aussi bien fonctionner sur d'autres serveurs / environnements également. Normalement, les utilisateurs utilisent des événements Application_Start ou Session_Start, etc. dans le fichier global.asax pour placer le code de licence là-bas. Il est tout à fait possible que l'événement Application_Start / Session_Start ne soit pas déclenché pour exécuter le code de licence dans leurs nouveaux emplacements. Il convient de noter ici qu'Aspose.Cells lancera toujours une exception si le composant ne parvient pas à trouver le fichier de licence dans un chemin. Les utilisateurs doivent s'assurer que le code de licence (où qu'ils le placent) doit être traité et que les événements devraient être déclenchés dans lesquels ils mettent le code de licence. L'utilisateur peut redémarrer le service associé, c'est-à-dire "Publication Web dans le monde entier", et essayer de tracer si les événements Application_Start / Session_Start sont déclenchés lorsqu'ils visitent leurs projets dans le nouvel environnement du serveur.

### **Confirmation**

Veuillez également vous assurer que…

- Vous utilisez un fichier de licence valide dans votre projet.
- Vous ou quelqu'un d'autre ne devez pas éditer / modifier le fichier de licence sinon le fichier de licence ne fonctionnera pas.
- Vous devez être conscient de l'expiration de votre abonnement de licence (vous pouvez simplement ouvrir le fichier lic dans le bloc-notes et vérifier la date d'expiration).
- Vous n'utilisez pas une version (Aspose.Cells.dll) qui a été publiée après l'expiration de votre abonnement de licence. Il convient de noter ici qu'un fichier de licence n'expire jamais, mais si vous utilisez la version du composant qui est sortie après l'expiration de votre abonnement, vous obtiendrez un avertissement de copyright d'évaluation supplémentaire chaque fois que vous créez un fichier Excel.

### **Références**

<https://forum.aspose.com/t/license-file-not-working-on-new-server/83110>

<https://forum.aspose.com/t/license-not-being-detected/83516/4>
