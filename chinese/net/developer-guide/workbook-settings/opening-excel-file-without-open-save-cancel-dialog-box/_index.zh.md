---
title: 在不显示打开保存取消对话框的情况下打开Excel文件
type: docs
weight: 150
url: /zh/net/opening-excel-file-without-open-save-cancel-dialog-box/
---

{{% alert color="primary" %}} 

本文介绍如何在浏览器中打开Microsoft Excel文件而不显示打开-保存-取消对话框。 

需要注意的是，不允许直接下载文件的安全限制是由Microsoft（或其他浏览器供应商）强制执行的，而不是由Aspose强制执行的。它是为了阻止并限制潜在有害的文件下载到本地机器。 

为客户的本地系统允许下载而不显示打开-保存-取消对话框对下载进行提示是有风险的。Aspose没有提供选项或解决方案，因为这将是一个非常大的安全风险。

{{% /alert %}} 
## **为什么是安全风险？**
当尝试下载文件时，Internet Explorer 显示的“打开-保存-取消”对话框如下图所示。

|**打开-保存-取消对话框**|
| :- |
|![todo:image_alt_text](opening-excel-file-without-open-save-cancel-dialog-box_1.png)|
正如前面所解释的，允许文件在系统上打开或运行而没有确认您确实希望这样做是一种安全风险。一些文件包含病毒，一些网站会尝试下载有害文件到您的计算机上而不发出提示。因此，不建议允许文件下载而没有下载提示，以便用户在下载或运行文件之前验证文件及其来源。禁用下载对话框会使系统容易受到病毒、木马和可能悄悄影响系统的黑客的威胁。 
## **在没有“打开-保存-取消”对话框的情况下打开文件**
虽然这是一个严重的安全问题，但微软仍提供允许用户禁用文件下载的“打开-保存-取消”提示的 Internet Explorer 设置。 

在 Windows 资源管理器中：

1. 在“工具”菜单中，选择“文件夹选项”。
1. 在“文件夹选项”对话框中点击“文件类型”选项卡。
1. 选择 XLS 扩展文件类型。
1. 点击“高级”。 
   一个对话框显示在屏幕上，并且在底部有三个选项。
1. 取消勾选“下载后确认打开”。
1. 选择第三个选项：“在相同窗口中浏览” - 在 Internet Explorer 中查看 Excel 文件而不启动独立的 Microsoft Excel。 

|**编辑文件类型选项**|
| :- |
|![todo:image_alt_text](opening-excel-file-without-open-save-cancel-dialog-box_2.png)|
此设置允许文件在网络浏览器中直接运行，无需在下载或打开文件时显示“打开-保存-取消”对话框。
