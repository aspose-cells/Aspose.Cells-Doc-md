---
title : "Security Exception Issue" 
description : "" 
weight : 12025 
toc : false
type: docs
url: /net/gettingstarted/knownissues/security+exception+issue/
---

# Aspose.Cells for .NET : Security Exception Issue


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Security Exception Problem](#security-exception-problem)
    *   1.1 [Explanation](#explanation)
    *   1.2 [Solution](#solution)
{{< /panel >}}
## Security Exception Problem

Some users may receive "Security Exception" error while trying to use Aspose.Cells. This problem is generally happened in a web application.

### Explanation

Aspose.Cells has to call some **Win32 GDI APIs** to provide some important features. If the web server has a strict trust level, this security exception may be thrown.

### Solution

Please try to create a new permission set to give Aspose.Cells.dll security permission with "Allow calls to unmanaged assemblies" enabled.

