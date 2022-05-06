# Matlab-and-ansys-integration

This is work is intendented to show the Integration of the Matlab and Ansys.
The methods include extracting a journal file from the Ansys workbench and editing according to the requirement.
The python run file calls ansys design points through framework directory instead of opening the GUI.

The work flow
1.Choose the parameter which need to varied and parametrise within the Ansys
2.Record the python journal file on the Ansys workbench from your simulation
3.Edit the journal file according to your requirement for chosen number of parameters
4.Create zip file of the Ansys workbench problem
5.Run it by python run.py (Ansys workbench framework directory needs to changed)
6.Now the this must be able to take the input from the input.txt file and the answer will be written to output.txt file.
