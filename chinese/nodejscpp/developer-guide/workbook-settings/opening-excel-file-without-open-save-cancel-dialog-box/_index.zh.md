---
title: 使用Node.js通过C++在没有“打开、保存、取消”对话框的情况下打开Excel文件
linktitle: 在没有打开保存取消对话框的情况下打开Excel文件
type: docs
weight: 150
url: /zh/nodejs-cpp/opening-excel-file-without-open-save-cancel-dialog-box/
--- 

{{% alert color="primary" %}} 

本文介绍了如何在浏览器中打开Microsoft Excel文件而不显示打开-保存-取消对话框。 

值得注意的是不允许直接下载文件的安全限制是由Microsoft（或其他浏览器供应商）强制执行的，而不是由Aspose强制执行的。 它是为了阻止和限制潜在有害文件被下载到本地机器。 

允许在不显示打开-保存-取消对话框的情况下下载对客户端本地系统来说是有风险的。 从Aspose那里没有任何选项或解决方法，因为这将是非常大的安全风险。

{{% /alert %}} 

## **为什么是安全风险?**
当尝试下载文件时，Internet Explorer显示的“打开-保存-取消”对话框如下图所示。

|**打开-保存-取消对话框**| 
| :- | 
|![todo:image_alt_text](opening-excel-file-without-open-save-cancel-dialog-box_1.png)| 
如前所述，允许文件在未确认的情况下在系统中打开或运行存在安全风险。有些文件含病毒，某些网站会在未提示的情况下试图下载有害文件到你的机器上。因此，不建议允许文件下载时跳过下载提示，以确保用户在下载或运行文件前能验证文件及其来源。禁用下载对话框会使系统易受病毒、特洛伊木马和黑客的攻击，他们可能会偷偷影响你的系统。 

## **在没有“打开-保存-取消”对话框的情况下打开文件**
尽管这是一个很大的安全问题，微软仍然提供了允许用户禁用文件下载的“打开-保存-取消”提示的Internet Explorer设置。 

在Windows资源管理器中：

1. 在“工具”菜单上，选择“文件夹选项”。
1. 在“文件夹选项”对话框中点击“文件类型”选项卡。
1. 选择XLS扩展文件类型。
1. 点击“高级”。 
   显示一个对话框，底部有三个选项。
1. 取消选中“下载后确认打开”。
1. 选择第三个选项 - “在同一窗口中浏览” - 以在Internet Explorer中查看Excel文件而不启动独立的Microsoft Excel。 

|**编辑文件类型选项**| 
| :- | 
|![todo:image_alt_text](opening-excel-file-without-open-save-cancel-dialog-box_2.png)| 
此设置允许文件在Web浏览器中直接运行，而无需下载或打开文件时显示“打开-保存-取消”对话框。 
{{< app/cells/assistant language="nodejs-cpp" >}}
