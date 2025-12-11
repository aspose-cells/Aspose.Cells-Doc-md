---
title: Loading event in GridDesktop
type: docs
weight: 1060
url: /net/aspose-cells-griddesktop/loading-event
description: This article describes how to use the loading event in GridDesktop.
keywords: GridDesktop,event,loading event,loading
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Loading event for GridDesktop**
The following sample code illustrates how to use different kinds of loading events for GridDesktop while importing a file. Please check the [sample excel file](loading-event.xlsx).

The file is password protected. First, we try to open it with an incorrect password, then finally, in the FailLoadFile event, we use the correct password to open it.

![result view of loading event](loadingevent.png)

### **Sample Code**
{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "LoadingEvent.cs" >}}
