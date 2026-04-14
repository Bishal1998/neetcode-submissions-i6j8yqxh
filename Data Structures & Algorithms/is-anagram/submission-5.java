class Solution {
    public boolean isAnagram(String s, String t) {

        Map<Character, Integer> map = new HashMap();

        //for s

        for (char c : s.toCharArray()){
            map.put(c, map.getOrDefault(c, 0) + 1);
        }

        //for t

        for (char c : t.toCharArray()){
            map.put(c, map.getOrDefault(c, 0) - 1);
        }

        System.out.println(map);

        for(int value : map.values()){
            if(value != 0){
                return false;
            }
        }

        return true;

    }
}
