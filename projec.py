import os
while True:
 print(
        """
        -------------------------------------------------------------------
                             DOCKER MENU BASED PROGRAM
        -------------------------------------------------------------------
        1.Launch new Container
        2.Stop the Container
        3.Remove the Container
        4.Start the Container
        5.Show only running container
        6.List all Container
        7.List all images
        8.Pull image from Docker hub
        9.Exit
        """)
 choice = input("Enter your choice :")
 if choice =="1":
   name = input("Enter name of container:")
   image= input("Enter the name of image:")
   os.system(f"docker run -dit --name={name} {image}")

 elif choice =="2":
  name = input("Enter name of container:")
  os.system(f"docker stop {name} ")

 elif choice =="3":
  name = input("Enter name of container:")
  os.system(f"docker rm -f {name}")

 elif choice =="4":
  name = input("Enter name of container:")
  os.system(f"docker rm start {name} ")

 elif choice =="5":
  os.system(f"docker ps")

 elif choice =="6":
  os.system(f"docker ps -a ")

 elif choice=="7":
  os.system(f"docker images")

 elif choice =="8":
  image = input("Enter name of image:")
  os.system(f" docker pull {image} ")

 elif choice =="9":
  os.system("exit")
  break