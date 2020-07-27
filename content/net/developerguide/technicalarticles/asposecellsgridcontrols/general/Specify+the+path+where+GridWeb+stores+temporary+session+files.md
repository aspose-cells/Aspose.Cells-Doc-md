+++
title = "Specify the path where GridWeb stores temporary session files" 
description = "" 
weight = 20341 
+++

Aspose.Cells for .NET : Specify the path where GridWeb stores temporary session files  

# Aspose.Cells for .NET : Specify the path where GridWeb stores temporary session files


When GridWeb session mode is ViewState, it stores its temporary session files inside the Application Base Directory. Sometimes, it is not OK to store temporary session files there because Application Base Directory might not have write permissions on it. In such cases, GridWeb throws such an exception

\[UnauthorizedAccessException: Access tothe path 'D:\\inetpub\\wwwroot\\AsposeExcelTest\\gwb\_tempGridWeb1' is denied.\]

The solution to above problem is to give write access to Application Base Directory or change the GridWeb temporary session files path having write access using the `GridWeb.SessionStorePath` property. This path should be relative to Application Base Directory.

## Specify the path where GridWeb stores temporary session files

The following sample code specifies the path where GridWeb stores temporary session files.

